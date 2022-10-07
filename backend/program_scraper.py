from typing import Dict, List, Tuple
import requests
from lxml import html
from tqdm import tqdm
import json
import unicodedata
from degree_util import depts, course_dict

# The api key is public so it does not need to be hidden in a .env file
BASE_URL = "http://rpi.apis.acalog.com/v1/"
# It is ok to publish this key because I found it online already public
DEFAULT_QUERY_PARAMS = "?key=3eef8a28f26fb2bcc514e6f1938929a1f9317628&format=xml"
CHUNK_SIZE = 500


# def get_credit(str):
#     for course in course_dict:
#         if (course["name"] == str):
#             if (len(course["credits"]))
#             return course["credits"]
#     return 0


# returns the list of catalogs with the newest one being first
# each catalog is a tuple (year, catalog_id) ex: ('2020-2021', 21)
def get_catalogs() -> List[Tuple[str, int]]:
    catalogs_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getCatalogs"
        ).text.encode("utf8")
    )
    catalogs = catalogs_xml.xpath("//catalogs/catalog")

    ret: List[Tuple[str, int]] = []
    # For each catalog get its year and id and add that as as tuples to ret
    for catalog in catalogs:
        catalog_id: int = catalog.xpath("@id")[0].split("acalog-catalog-")[1]
        catalog_year: str = catalog.xpath(".//title/text()")[0].split(
            "Rensselaer Catalog "
        )[1]
        ret.append((catalog_year, catalog_id))

    # sort so that the newest catalog is always first
    ret.sort(key=lambda tup: tup[0], reverse=True)
    return ret


# Returns a list of program ids for a given catalog
def get_program_ids(catalog_id: str) -> List[str]:
    programs_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}search/programs{DEFAULT_QUERY_PARAMS}&method=listing&options[limit]=0&catalog={catalog_id}"
        ).text.encode("utf8")
    )
    return programs_xml.xpath('//result[type="Baccalaureate"]/id/text()')

# <<< need rework for programs >>>
def course_from_string(inp, depts):
    for dept in depts:
        fnd = inp.find(dept)
        if fnd != -1:
            if inp[fnd+8].isdigit() or inp[fnd+8] == "X":
                if inp[fnd+5] != '6':
                    return inp[fnd:fnd+4] + inp[fnd+5:fnd+9]


# def handle_electives(cont, courses, depts, year):
#     level = '0'
#     for char in cont:
#         if char.isdigit():
#             level = char
#             break;
#     if level == '0':
#         return
#     subj = "TEMP"
#     for word in cont.split():
#         if word in depts:
#             subj = word
#             break
#     if subj == "TEMP":
#         return
    # path = '../../frontend/src/data/json/' + str(year)
    # f = open(path + '/courses.json', 'r')
    # all_courses = json.load(f)
    # for course in all_courses:
    #     ID = all_courses[course]["ID"]
    #     subjC = all_courses[course]["subj"]
    #     if ID[0] == level and subjC == subj:
    #         courses[course.encode("ascii", "ignore").strip().decode().strip()] = subjC+ID
    # f.close()

# Normalize a string, using unicode data. Remove all weird whitespace tag 
def norm_str(str):
    return unicodedata.normalize("NFKD",str).strip().replace('\n',' ').replace('\t','')

# Take a list of list and remove empty list elements
def striplist(lstr): 
    return list(filter(None, lstr))


def split_content(str):
    ret = []
    while (str.find("Credit Hours") != -1):
        tmp = str.find("Credit Hours") + 16
        ret.append(norm_str(str[:tmp]))
        str = str[tmp:]
    return ret

def rem_footnote(str):
    while (str.find("(See footnote") != -1):
        str = str[:str.find("(See footnote")] + str[str.find("(See footnote") + 23:]
    return str

def rem_arch(str):
    s = "ExceptionProcess."
    if (str.find(s) != -1):
        str = str[str.find(s) + len(s):]
    return str

def rem_all(str):
    return rem_footnote(rem_arch(str))

# takes in xml file of of one semester of courses
# input:  core.xpath("./children/core")   ==>> cores->core->children->core
def parse_semester(inp):
    ret = []
    for classes in inp:
        sem = []
        content = classes.xpath("./content")
        for c in content:
            tmp = split_content(rem_all(c.text_content()))
            sem.extend(tmp)
        block = classes.xpath("./courses/include")
        for b in block:
            if (len(b.text_content()) > 0):
                s = norm_str(b.text_content())
                sem.append(s)
        if (len(striplist(sem)) > 0):
            ret.append(striplist(sem))
    return ret

def parse_template(semesters): 
    sems = {}
    count = 1
    sem = 0
    extra = []
    for item in semesters:
        template_str = str(count) + "-"
        if count > 4:
            extra.extend(item)
        else:
            if count != 3:
                if sem == 0:
                    template_str += "Fall"
                    sem = 1
                elif sem == 1:
                    template_str += "Spring"
                    count = count + 1
                    sem = 0
            else:
                if sem == 0:
                    template_str += "Summer"
                    sem = 1
                elif sem == 1:
                    template_str += "Fall or Spring"
                    count = count + 1
                    sem = 0
            sems[template_str] = item
    sems["Extra"] = extra
    return sems


def parse_courses(core, name, year):
    courses = []
    tmp = core.xpath("./content/ul/li/descendant-or-self::*/text()")
    tmp += core.xpath("./courses/adhoc/content/ul/li/descendant-or-self::*/text()")
    tm = core.xpath("./children/core")
    courses = parse_semester(core.xpath("./children/core"))
    # print(t)
    # for t in tmp:
    #     app = False
    #     for s in t.split():
    #         if s in depts:
    #             app = True
    #     if app:
    #         t = (t.strip())
    #         t = t.encode("ascii", "ignore").strip().decode().strip()
    #         content.append(t)
    # if not(len(content) == 0):
    #     for cont in content:
    #         if "transfer" in name.lower():
    #             crs = cont + "XXXX"
    #             courses[crs] = crs
    #         # handle as an elective meaning we will have to some funky stuff
    #         elif "elective" in cont.lower() or "any" in cont.lower() or "level" in cont.lower():
    #             handle_electives(cont, courses, depts, year)
    #         else:
    #             subjID = course_from_string(cont, depts)
    #             name = ""
    #             if "-" in cont:
    #                 name = cont.split("-", 1)[1].strip()
    #             else:
    #                 name = cont.split(subjID[4:])[1].strip()
    #             courses[name] = subjID
    # courses_xml = core.xpath("./courses/include/fallback/title/text()")

    # for course in courses_xml:
    #     # fixes all weird unicode and stuff
    #     course = course.strip().encode("ascii", "ignore").strip().decode()
    #     subjID = course_from_string(course, depts)
    #     name = course.split("-", 1)[1].split("Credit")[0].strip()
    #     courses[name] = subjID
    return courses

def get_program_data(pathway_ids: List[str], catalog_id, year) -> Dict:
    data = {}
    ids = "".join([f"&ids[]={path}" for path in pathway_ids])
    url = f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getItems&options[full]=1&catalog={catalog_id}&type=programs{ids}"
    pathways_xml = html.fromstring(requests.get(url).text.encode("utf8"))

    pathways = pathways_xml.xpath("//programs/program[not(@child-of)]");
    for pathway in pathways:
        courses = []
        name = pathway.xpath("./title/text()")[0].strip()
        if (name != "Computer Science"):
            continue
        desc = ""
        if len(pathway.xpath("./content/p/text()")) >= 1:
            desc = pathway.xpath("./content/p/text()")[0].strip()
            desc = ' '.join(desc.split())
        cores = pathway.xpath("./cores/core")
        cores += pathway.xpath("./cores/core/children/core")

        for core in cores:
                courses.extend(parse_courses(core, name, year))
                # if "required" in anchor_name:
                #     courses = parse_courses(core, name, year)
                #     data[name]["Required"] = courses
                # elif "oneof" in anchor_name:
                #     courses = parse_courses(core, name, year)
                #     one_of_name = "One Of" + str(one_of_index)
                #     data[name][one_of_name] = courses
                #     one_of_index += 1
                # elif "minor" in anchor_name:
                #     minors = list(filter(lambda x: x != "", \
                #      [minor.replace("Minor", "").replace("minor", "").encode("ascii", "ignore").strip().decode() \
                #      for minor in core.xpath("./content/descendant::*/text()")]))
                #     data[name]["minor"] = minors
                # else:
        # get rid of duplicates (if it shows up in required, we don't want it to be optional too)
        # if "Required" in data[name]:
        #     for req in data[name]["Required"]:
        #         for type in data[name]:
        #             if (type == "Remaining" or type[0:6] == "One Of") and req in data[name][type]:
        #                 del data[name][type][req]
        template = parse_template(courses)
        data[name] = {
                "name": name,
                "description": desc,
                "credits" : 128,
                "template": template
            }

    return data

def scrape_pathways():
    print("Starting pathway scraping")
    catalogs = get_catalogs()
    # take the most recent catalog
    catalogs = catalogs[:1]

    # Scraping catalogs
    programs_per_year = {}
    for index, (year, catalog_id) in enumerate(tqdm(catalogs)):
        program_ids = get_program_ids(catalog_id)
        # scraing the program (degree)
        data = get_program_data(program_ids, catalog_id, year)
        programs_per_year[year] = data
    print("Finished program scraping")

    # create JSON obj and write it to file
    json_object = json.dumps(programs_per_year, indent=4)
    with open("programs.json", "w") as outfile:
        outfile.write(json_object)
    return programs_per_year

if __name__ == "__main__":
    scrape_pathways()