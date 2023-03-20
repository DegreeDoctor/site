from typing import Dict, List, Tuple
import requests
from lxml import html
from tqdm import tqdm
import json
from degree_util import mnrs, root
from degree_util import get_catalogs, norm_str, word_to_num, rep_uni
from collections import OrderedDict
# The api key is public so it does not need to be hidden in a .env file
BASE_URL = "http://rpi.apis.acalog.com/v1/"
# It is ok to publish this key because I found it online already public
DEFAULT_QUERY_PARAMS = "?key=3eef8a28f26fb2bcc514e6f1938929a1f9317628&format=xml"
CHUNK_SIZE = 500

def write_file(text, file):
    with open(file, "w") as out:
        out.write(text)

# Returns a list of program ids for a given catalog
def get_program_ids(catalog_id: str) -> List[str]:
    programs_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}search/programs{DEFAULT_QUERY_PARAMS}&method=listing&options[limit]=0&catalog={catalog_id}"
        ).text.encode("utf8")
    )
    return programs_xml.xpath('//result[type="Minor"]/id/text()')

def trim_crn(inp):
    return inp[inp.find("-")+1:].strip()

def get_minor_data(program_ids: List[str], catalog_id) -> Dict:
    data = {}
    # Break the courses into chunks of CHUNK_SIZE to make the api happy
    ids = "".join([f"&ids[]={path}" for path in program_ids])
    url = f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getItems&options[full]=1&catalog={catalog_id}&type=programs{ids}"

    program_xml = html.fromstring(requests.get(url).text.encode("utf8"))

    programs = program_xml.xpath("//programs/program[not(@child-of)]");
    for program in programs:

        # included to skip programs that either have really bad edge cases/are super specific programs
        # to be decided on a later date if it is worth to refactor code for (and to keep a list of really)
        # broken but small programs
        check = False
        for mnr in mnrs:
            if (name == mnr):
                check = True
        if (check):
            continue
        
        # rest of parsing
        name = norm_str(program.xpath("./title/text()")[0].strip())
        description = rep_uni(norm_str(program.xpath("./content")[0].text_content().strip()))
        if (len(description) == 0):
            description = rep_uni(norm_str(program.xpath("./cores/core/content")[0].text_content().strip()))
        rest = program.xpath("./cores/core")

        for r in rest: 
            children = r.xpath("./children/core")
            rest.extend(children)

        # if (name != "Cognitive Science of Artificial Intelligence Minor"):
        #     continue

        requirements = []

        for r in rest:

            required = {}
            course_list = []

            title = r.xpath("./title/text()")
            tmp = norm_str(title[0])
            content = r.xpath("./content")
            content_s = norm_str(content[0].text_content())
            courses = r.xpath("./courses/include")

            tmp = tmp.replace("Plus","Choose").replace("And","Choose").replace("Remaining","Choose 3")
            tmp = tmp.replace("Students must also ","").replace("Prerequisites:","Required:")
            tmp = tmp.replace("Take two","Choose two").replace("Take all","Required")
            tmp = tmp.replace(" remaining credits from the following with at least","")
            content_s = content_s.replace("Students must complete:","Required ")

            if (content_s.upper().find("COMPLETE") != -1):
                # tmp_s is the word after 'Complete'
                tmp_s = content_s[content_s.upper().find("COMPLETE")+9:]
                tmp_s = tmp_s[:tmp_s.find(" ")]
                required["amount"] = word_to_num(tmp_s) 
            elif(tmp.upper().find("COMPLETE") != -1):
                tmp_s = tmp[tmp.upper().find("COMPLETE")+9:]
                tmp_s = tmp_s[:tmp_s.find(" ")]
                required["amount"] = word_to_num(tmp_s) 
            elif (tmp.upper().find("REQUIRE") != -1 or content_s.upper().find("REQUIRE") != -1):
                required["amount"] = len(courses)
            else:
                if (tmp.upper().find("CHOOSE") != -1):
                    tmp = tmp.replace("at least ","")
                    tmp = tmp[tmp.find(" ")+1:]
                    tmp = ''.join([x for x in tmp if x.isalnum() or x.isspace()])

                tmp_s = tmp.lower()[:tmp.find(" ")] if tmp.find(" ") != -1 else tmp.lower()
                if (tmp_s != word_to_num(tmp_s)):
                    required["amount"] = word_to_num(tmp_s)  

            for course in courses:
                course_list.append(trim_crn(norm_str(course.text_content())))
                
            if required["amount"] != None and (required["amount"] == 8 or required["amount"] == 16 or required["amount"] == 12):
                required["amount"] /= 4
                required["amount"] = int(required["amount"])

            required["courses"] = course_list
            if (len(course_list) > 0):
                requirements.append(required)

        data[name] = {
            "name": name,
            "description": description,
            "requirements": requirements
        }

    return data

def scrape_programs():
    print("Starting program scraping")
    num_catalog = 1
    catalogs = get_catalogs()
    # take the most recent num_catalog catalogs
    catalogs = catalogs[:num_catalog]

    # Scraping catalogs
    programs_per_year = {}
    for index, (year, catalog_id) in enumerate(tqdm(catalogs)):
        # print(year)
        program_ids = get_program_ids(catalog_id)
        data = get_minor_data(program_ids, catalog_id)
        # scraing the program (degree)
        programs_per_year[year] = data
    print("Finished program scraping")
    # create JSON obj and write it to file
    json_object = json.dumps(programs_per_year,sort_keys=True, indent=2, ensure_ascii=False)
    with open(root + "/backend/data/test.json", "w") as outfile:
        outfile.write(json_object)
    return programs_per_year

if __name__ == "__main__":
    scrape_programs()