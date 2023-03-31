#hey guys its me the professor scraper 😈😈😈

import json
import requests
import math
import aiohttp
from tqdm import tqdm

BASE_URL = "http://www.ratemyprofessors.com/filter/professor/?&page="
DEFAULT_PARAMS = "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=795"

async def get_profs():
    profs = {}
    page = requests.get(f"{BASE_URL}1{DEFAULT_PARAMS}")
    json_page = json.loads(page.content)
    num_pages = math.ceil(json_page['searchResultsTotal'] / 20)
    for index in tqdm(range(num_pages + 1)):
        page = requests.get(f"{BASE_URL}{index}{DEFAULT_PARAMS}")
        json_page = json.loads(page.content)
        for prof_index in json_page['professors']:
            temp_dict = {}
            temp_dict['rating'] = prof_index['overall_rating']
            temp_dict['num_ratings'] = prof_index['tNumRatings']
            temp_dict['rmp_id'] = prof_index['tid']
            prof_Fname = prof_index['tFname']
            prof_Mname = prof_index['tMiddlename']
            prof_Lname = prof_index['tLname']
            if prof_Mname == "":
                prof_name = f"{prof_Fname} {prof_Lname}"
            else:
                prof_name = f"{prof_Fname} {prof_Mname} {prof_Lname}"
            profs[prof_name] = temp_dict
    return profs
    

async def scrape_RMP(folder_path):
    profs = await get_profs()
    f = open(folder_path + 'professors.json', 'w')
    json.dump(profs, f, sort_keys=True, indent=2, ensure_ascii=False)
    f.close()

