from typing import Dict, List, Tuple
import requests
from lxml import html
from tqdm import tqdm
import json
import unicodedata
from degree_util import depts, course_dict
from collections import OrderedDict

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
    return unicodedata.normalize("NFKD",str).strip()

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
        str = str[:str.find("(See footnote")] + str[str.find("(See footnote") + 22:]
    return str

def rem_arch(str):
    s = "ExceptionProcess."
    if (str.find(s) != -1):
        str = str[str.find(s) + len(s):]
    return str

def rem_all(str):
    return rem_footnote(rem_arch(str))

def parse_template(semesters): 
    sems = OrderedDict()
    curr_year = 1
    first_sem_in_year = True
    extra = []
    for item in semesters:
        template_str = str(curr_year) + "-" 
        # Extra content 
        if curr_year > 4:
            extra.extend(item)
            continue
        # Year 1,2 and 4
        if curr_year != 3:
            if first_sem_in_year:
                template_str += "Fall"
            elif not first_sem_in_year:
                template_str += "Spring"
                curr_year += 1
            first_sem_in_year = not first_sem_in_year
        else:
            if first_sem_in_year:
                template_str += "Summer"
            elif not first_sem_in_year:
                template_str += "Fall or Spring"
                curr_year += 1
            first_sem_in_year = not first_sem_in_year 
        sems[template_str] = item
    sems["Extra"] = extra
    return sems

def get_dept(str):
    for dept in depts: 
        fnd = str.find(dept)
        if fnd != -1:
            return str[fnd:fnd+4]
    return ""

def replace_dept(str):
    if str == "CS" or str == "Computer Science":
        return "CSCI"
    if str == "Mathematics":
        return "MATH"
    return str

def get_elec(str):
    ret = []
    spltstr = str.split(" or ")
    for s in spltstr:
        fnd_e = s.find("Elective")
        fnd_o = s.find("Option")
        if fnd_e != -1:
            ret.append(replace_dept(s[0:fnd_e-1]))
        if fnd_o != -1:
            ret.append(replace_dept(s[0:fnd_o-1]))
    return ret

def generate_credits(inp):
    ret = {}
    for i in range(0,8):
        for c in inp[i]:
            if (len(get_dept(c)) > 0):
                print(c)
            else:
                tmp = get_elec(c)
                for t in tmp:
                    if ret.get(t) != None:
                        ret[t] += 4
                    else: 
                        ret[t] = 4
    print(ret)
    
        

# takes in xml file of of one semester of courses
# input:  core.xpath("../cores/core/children/core")  
def parse_semester(inp):
    ret = []
    for classes in inp:
        title =classes.xpath("./title")
        title = title[0].text_content().strip()
        
        if title.count("Fall") == 0 and title.count("Spring") == 0 and title.count("Arch") == 0:
            content = classes.xpath("./content")
            content_txt = content[0].text_content().strip()
            
            ret.append([title, norm_str(content_txt)])

        else:
            sem = []
            # Parsing electives include: Free electives, Hass electives, Capstones
            electives = classes.xpath("./content")
            for c in electives:
                tmp = split_content(rem_all(c.text_content()))
                sem.extend(tmp)
                    
            # Parsing Major course
            block = classes.xpath("./courses")
            for b in block: 
                content = b.xpath("./include")
                adhoc = b.xpath("./adhoc/content")
                extra = ""
                s = ""
                for a in adhoc: 
                    if (len(rem_all(a.text_content())) > 0):
                        extra += rem_all(a.text_content())
                for c in content:
                    if (len(c.text_content()) > 0):
                        s = norm_str(c.text_content())
                        if (len(extra) > 0):
                            if (extra[0] == " "):
                                s += extra
                            else:
                                s += " " + extra
                        sem.append(s)

            course_list = striplist(sem)
            if (len(course_list) > 0):
                ret.append(course_list)
    return ret

def parse_courses(core, name, year):
    # Get an array of all semesters and parse them
    semester_list = core.xpath("./children/core")
    courses = parse_semester(semester_list)
    return courses

def get_program_data(pathway_ids: List[str], catalog_id, year) -> Dict:
    data = {}
    ids = "".join([f"&ids[]={path}" for path in pathway_ids])
    url = f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getItems&options[full]=1&catalog={catalog_id}&type=programs{ids}"
    pathways_xml = html.fromstring(requests.get(url).text.encode("utf8"))

    pathways = pathways_xml.xpath("//programs/program[not(@child-of)]");
    # For every Major degree
    for pathway in pathways:
        courses = []
        name = pathway.xpath("./title/text()")[0].strip()

        # For now only parse CS
        if (name != "Computer Science"):
            continue
        
        # Get program description
        desc = ""
        if len(pathway.xpath("./content/p/text()")) >= 1:
            desc = pathway.xpath("./content/p/text()")[0].strip()
            desc = ' '.join(desc.split())
        
        # Get the list of years in the program
        cores = pathway.xpath("./cores/core")

        # Parse each school year for courses
        for core in cores:
            courses.extend(parse_courses(core, name, year))
        generate_credits(courses)
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
    num_catalog = 1
    catalogs = get_catalogs()
    # take the most recent num_catalog catalogs
    catalogs = catalogs[:num_catalog]

    # Scraping catalogs
    programs_per_year = {}
    for index, (year, catalog_id) in enumerate(tqdm(catalogs)):
        # print(year)
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