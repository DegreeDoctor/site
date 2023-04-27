import json
import os
import unicodedata
from typing import List, Tuple
import requests
from lxml import html
from tqdm import tqdm

# The api key is public so it does not need to be hidden in a .env file
BASE_URL = "http://rpi.apis.acalog.com/v1/"
# It is ok to publish this key because I found it online already public
DEFAULT_QUERY_PARAMS = "?key=3eef8a28f26fb2bcc514e6f1938929a1f9317628&format=xml"
CHUNK_SIZE = 500

# uniform filepath for all backend routing
filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
root = os.path.dirname(filepath)
# Opens the subjects.JSON and returns a list of subject code

# Returns a list of program ids for a given catalog
def get_program_ids(catalog_id: str, type_query : str) -> List[str]:
    programs_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}search/programs{DEFAULT_QUERY_PARAMS}&method=listing&options[limit]=0&catalog={catalog_id}"
        ).text.encode("utf8")
    )
    return programs_xml.xpath('//result[type="' + type_query + '"]/id/text()')

def get_subjs():
    subjs = []
    f = open(root + '/backend/data/subjs.json', 'r') #make sure to close at end of file
    tmp = json.load(f)
    for subj in tmp:
        subjs.append(subj)
    f.close()
    return subjs

# subject object
subjs = get_subjs()

# gets courses from courses.json for programs logic
def get_courses():
    f = open(root + '/frontend/src/data/courses.json','r')
    ret = json.load(f)
    f.close()
    return ret

# course object
course_dict = get_courses()

#  gets list of skipped programs
def get_prgms():
    prgms = []
    f = open(root + '/backend/data/skip_prgms.json', 'r')
    tmp = json.load(f)
    for prgm in tmp:
        prgms.append(prgm)
    f.close()
    return prgms

prgms = get_prgms()

# gets list of skipped minors
def get_mnrs():
    mnrs = []
    f = open(root + '/backend/data/skip_mnrs.json','r')
    tmp = json.load(f)
    for mnr in tmp:
        mnrs.append(mnr)
    f.close()
    return mnrs

mnrs = get_mnrs()

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
    
# QOL functions 

# removes non alphanumeric and space characters
def clean_str(s: str) -> str:
    return "".join([x for x in s if x.isalnum() or x.isspace()])

# replaces various unicode text artifacts found on the catalog dataset.
def rep_uni(str):
    return str.replace("\n","").replace("\t","").replace("\u200b","").replace("\u2013","").replace("\u00ad","").replace("\r","")

# Normalize a string, using unicode data. Remove all weird whitespace tag 
def norm_str(str):
    s1 = unicodedata.normalize("NFKD",str).strip()
    return rep_uni(s1)

# Take a list of list and remove empty list elements
def rem_empty(lstr): 
    return list(filter(None, lstr))

# Trims extraneous spaces
def trim_space(str):
    while (str.find("  ") != -1):
        str = str.replace("  "," ");
    return str

# trims course to only the course name
def trim_crn(inp):
    return inp[inp.find("-")+1:].strip()

# converts given words in input to their number counterparts
def word_to_num(inp):
    help_dict = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0',
    }
    if (inp.isnumeric()):
        return int(inp)
    if (inp not in help_dict.keys()):  
        return
    return int(''.join(help_dict[ele] for ele in inp.split()))