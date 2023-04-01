from typing import Dict, List
import requests
from lxml import html
from tqdm import tqdm
import json
from degree_util import mnrs, root
from degree_util import get_catalogs, norm_str, word_to_num, rep_uni
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
        
        data[name] = {
            "name": name,
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
    with open(root + "/backend/data/test.json", "w") as outfile:
        outfile.write(json_object)
    return pathways_per_year

if __name__ == "__main__":
    scrape_programs()