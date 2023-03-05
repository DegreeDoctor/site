from typing import Dict, List, Tuple
import requests
from lxml import html
from tqdm import tqdm
import json
import unicodedata
from degree_util import subjs, prgms, course_dict, root
from degree_util import get_catalogs, norm_str, rem_empty, clean_str, trim_space
from collections import OrderedDict

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
    with open(root + "/backend/data/type.xml","w") as outfile:
            outfile.write(str(html.tostring(programs_xml)))

    return programs_xml.xpath('//result[type="Minor"]/id/text()')

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
        # scraing the program (degree)
        # programs_per_year[year] = data
    print("Finished program scraping")

    # create JSON obj and write it to file
    json_object = json.dumps(programs_per_year,sort_keys=True, indent=2, ensure_ascii=False)
    # with open(root + "/backend/data/test.json", "w") as outfile:
    #     outfile.write(json_object)
    return programs_per_year

if __name__ == "__main__":
    scrape_programs()