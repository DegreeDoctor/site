from typing import Dict, List
import requests
from lxml import html
from tqdm import tqdm
import json
from degree_util import root
from degree_util import get_catalogs, norm_str, word_to_num, rep_uni, trim_crn
# The api key is public so it does not need to be hidden in a .env file
BASE_URL = "http://rpi.apis.acalog.com/v1/"
# It is ok to publish this key because I found it online already public
DEFAULT_QUERY_PARAMS = "?key=3eef8a28f26fb2bcc514e6f1938929a1f9317628&format=xml"
CHUNK_SIZE = 500

# Returns a list of program ids for a given catalog
def get_program_ids(catalog_id: str) -> List[str]:
    programs_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}search/programs{DEFAULT_QUERY_PARAMS}&method=listing&options[limit]=0&catalog={catalog_id}"
        ).text.encode("utf8")
    )
    return programs_xml.xpath('//result[type="Integrative Pathway"]/id/text()')

def get_pathway_data(program_ids: List[str], catalog_id) -> Dict:
    data = {}
    # Break the courses into chunks of CHUNK_SIZE to make the api happy
    ids = "".join([f"&ids[]={path}" for path in program_ids])
    url = f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getItems&options[full]=1&catalog={catalog_id}&type=programs{ids}"

    program_xml = html.fromstring(requests.get(url).text.encode("utf8"))

    # get each minor program XML object
    programs = program_xml.xpath("//programs/program[not(@child-of)]");
    for program in programs:
        name = norm_str(program.xpath("./title/text()")[0].strip())
        description = rep_uni(norm_str(program.xpath("./content")[0].text_content().strip()))
        if (len(description) == 0):
            description = rep_uni(norm_str(program.xpath("./cores/core/content")[0].text_content().strip()))
        
        # gets all of the core components
        rest = program.xpath("./cores/core")
        for r in rest: 
            children = r.xpath("./children/core")
            rest.extend(children)
        
        requirements = []
        course_sum = 0

        for r in rest:

            required = {}
            course_list = []

            # fetch the title, content, and courses XML paths
            title = r.xpath("./title/text()")
            tmp = norm_str(title[0])
            content = r.xpath("./content")
            content_s = norm_str(content[0].text_content())
            courses = r.xpath("./courses/include")
            adhocc = r.xpath("./courses/adhoc/content")

            extra = r.xpath("./courses");
            extra_arr = [];
            for e in extra:
                extra_arr.append(trim_crn(norm_str(e.text_content())));     

            # massaging the inputs to follow a standard input such that 
            # parsing is possible
            rem = 3 - course_sum if course_sum < 3 else 0

            tmp = tmp.replace("Remaining","Choose " + str(rem)).replace("Choose remaining","Choose " + str(rem))
            tmp = tmp.replace("Select ","Choose ")

            # two main cases: required classes vs chosen credit amounts per class
            if (content_s.upper().find("COMPLETE") != -1):

                tmp_s = content_s[content_s.upper().find("COMPLETE")+9:]
                tmp_s = tmp_s[:tmp_s.find(" ")]
                required["amount"] = word_to_num(tmp_s) 

            #  check for complete keyword
            elif(tmp.upper().find("COMPLETE") != -1):

                tmp_s = tmp[tmp.upper().find("COMPLETE")+9:]
                tmp_s = tmp_s[:tmp_s.find(" ")]
                required["amount"] = word_to_num(tmp_s) 

            # checks for required keyword
            elif (tmp.upper().find("REQUIRE") != -1 or content_s.upper().find("REQUIRE") != -1):

                required["amount"] = len(courses)
                for a in adhocc:
                    cont = norm_str(a.text_content())
                    if (cont.upper().find("OR") != -1):
                        required["amount"] -= 1
                        break

            else:
                tmp_s = ""
                
                #  checks for choose keyword 
                if (tmp.upper().find("CHOOSE") != -1):
                    tmp = tmp.replace("at least ","")
                    tmp = tmp[tmp.find(" ")+1:]
                    tmp = ''.join([x for x in tmp if x.isalnum() or x.isspace()])
                    tmp_s = tmp.lower()[:tmp.find(" ")] if tmp.find(" ") != -1 else tmp.lower()

                else:
                    tmp_s = tmp.lower()[:tmp.find(" ")] if tmp.find(" ") != -1 else tmp.lower()
               
                # check if the input is an integer otherwise set to default 0 value
                if (isinstance(word_to_num(tmp_s),int)):
                    required["amount"] = word_to_num(tmp_s)
                else:
                    required["amount"] = 0 

            # add all courses for current chunk to courselist
            for course in courses:
                course_list.append(trim_crn(norm_str(course.text_content())))
            
            # if the number of unique courses differs from the number of courses, we have a duplicate
            if (len(course_list) != len(list(set(course_list)))):
                course_list = list(set(course_list))
                
            # we want to reduce all formats from credits -> class amount so we just hard check for it
            if required["amount"] != None and (required["amount"] == 8 or required["amount"] == 16 or required["amount"] == 12):
                required["amount"] /= 4
                required["amount"] = int(required["amount"])

            # check the sum of all courses we have parsed so far
            course_sum += required["amount"] if (required["amount"] != None) else 0
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
    pathways_per_year = {}
    for index, (year, catalog_id) in enumerate(tqdm(catalogs)):
        # print(year)
        program_ids = get_program_ids(catalog_id)
        data = get_pathway_data(program_ids, catalog_id)
        # scraing the program (degree)
        pathways_per_year[year] = data
    print("Finished program scraping")
    # create JSON obj and write it to file
    json_object = json.dumps(pathways_per_year,sort_keys=True, indent=2, ensure_ascii=False)
    with open(root + "/frontend/src/data/pathways.json", "w") as outfile:
        outfile.write(json_object)
    return pathways_per_year

if __name__ == "__main__":
    scrape_programs()