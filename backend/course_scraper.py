# This scraper is mainly sourced from the QUACs team and
# is a modified version of their catalog scraper

from typing import Dict, List, Tuple
import requests
import sys
from lxml import html
import os
from tqdm import tqdm
import json
from lxml import etree
import csv

# The api key is public so it does not need to be hidden in a .env file
BASE_URL = "http://rpi.apis.acalog.com/v1/"
# It is ok to publish this key because I found it online already public
DEFAULT_QUERY_PARAMS = "?key=3eef8a28f26fb2bcc514e6f1938929a1f9317628&format=xml"
CHUNK_SIZE = 500
def get_depts():
    depts = []
    f = open('depts.json', 'r')
    f = json.load(f)
    for dept in f:
        depts.append(dept)
    return depts

depts = get_depts()
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


# Returns a list of course ids for a given catalog
def get_course_ids(catalog_id: str) -> List[str]:
    courses_xml = html.fromstring(
        requests.get(
            f"{BASE_URL}search/courses{DEFAULT_QUERY_PARAMS}&method=listing&options[limit]=0&catalog={catalog_id}"
        ).text.encode("utf8")
    )
    return courses_xml.xpath("//id/text()")


# Finds and returns a cleaned up description of the course
def get_catalog_description(fields, course_name):
    found_name = False
    # The description is always the next full field after the course name field
    # Itearte through the fields until we find the course name field and then return the next filled field
    for field in fields:
        if found_name == False:
            name = field.xpath(".//*/text()")
            if name and name[0] == course_name:
                found_name = True
        else:
            description = field.xpath(".//*/text()")
            if description:
                clean_description = " ".join(" ".join(description).split())
                # Short descriptions are usually false positives
                if clean_description.startswith("Prerequisite"):
                    return ""
                elif len(clean_description) > 10:
                    return clean_description.encode("ascii", "ignore").strip().decode().strip()

    return ""
# function should return an object where object = 
# ["required" = [Calc1, Calc2...], "One of" = [[Option 1, Option 2], [Option 1, Option 2]]]
def checkreq(list):
    for dept in depts:
        if list.find(dept + ' ') != -1 and list[list.find(dept)+5]:
            if list.find(dept + ' ') + 5 < len(list):
                if list[list.find(dept)+5].isdigit():
                    return True
    return False


def split_req(str):
    reqset = str.split(" AND ")
    final = []
    for req in reqset:
        new = req.split(" OR ")
        for n in new:
            if not checkreq(n):
                new.remove(n)
        final.append(new)
    return final
  
def get_prereq(str): 
    reqs = []
    one_of = []
    reqset = split_req(str)
    for req in reqset:
        if len(req) > 1:
            for r in req:
                one_of.extend(courses_from_string(r))
        else:
            reqs.extend(courses_from_string(''.join(req)))
    return { "req" : reqs, "one_of" : one_of }
def get_credit(str):
    credit = []
    if str.find("to") != -1:
        for x in range(int(str[:1]),int(str[len(str)-1:])+1):
            credit.append(x)
    elif str.isdigit():
        credit.append(int(str))
    return credit

def courses_from_string(inp):
    # REFACTOR (Clean up instead of searching from all dept)
    crses = set()
    for dept in depts:
        sp = inp.split(dept)
        if len(sp) > 1: 
            for item in sp: 
                if item[1:5].isdigit():
                    crses.add(dept + '-' + item[1:5])
    return list(crses)

def get_course_data(course_ids: List[str], catalog_id) -> Dict:
    data = {}
    # Break the courses into chunks of CHUNK_SIZE to make the api happy
    course_chunks = [
        course_ids[i : i + CHUNK_SIZE] for i in range(0, len(course_ids), CHUNK_SIZE)
    ]

    for chunk in course_chunks:
        ids = "".join([f"&ids[]={id}" for id in chunk])
        url = f"{BASE_URL}content{DEFAULT_QUERY_PARAMS}&method=getItems&options[full]=1&catalog={catalog_id}&type=courses{ids}"

        courses_xml = html.fromstring(requests.get(url).text.encode("utf8"))
        courses = courses_xml.xpath("//courses/course[not(@child-of)]")
        
        for course in courses:
            subj = course.xpath("./content/prefix/text()")[0].strip()
            if not (subj in depts):
                continue
            ID = course.xpath("./content/code/text()")[0].strip()
            if ID[0] == '6':
                continue
            course_name = course.xpath("./content/name/text()")[0].strip()
            fields = course.xpath("./content/field")
            offered_text = ""
            year = ""
            semesters = []
            cross_listed = []
            prereqs = []
            credit = []

            
            base = int(fields[0].get('type')[-3:])
            for field in fields:
                field_text = field.xpath("./descendant-or-self::*/text()")
                if len(field_text) > 0:
                    field_text = field_text[0].strip()
                    if field.get('type')[-3:] == str(base - 4): 
                        credit = get_credit(field_text)
                    elif field.get('type')[-3:] == str(base - 8):
                        if len(field_text) > 0:
                            cross_listed = courses_from_string(field_text.upper())
                            for item in cross_listed:
                                if item.find(subj + '-' + str(ID)) != -1:
                                    cross_listed.remove(item)
                    elif field.get('type')[-3:] == str(base - 11):
                        if "fall" in field_text.lower():
                            semesters.append("fall")
                        if "spring" in field_text.lower():
                            semesters.append("spring")
                        if "summer" in field_text.lower():
                            semesters.append("summer")
                        if "even" in field_text.lower():
                            year = "even"
                        if "odd" in field_text.lower():
                            year = "odd"
                        if "instructor" in field_text.lower():
                            year = "UIA"
                        if len(year) == 0:
                            year = "all"
                        offered_text = field_text
                    elif field.get('type')[-3:] == str(base - 13):
                        if len(field_text) > 0:
                            prereqs = get_prereq(field_text.upper())

            data[course_name] = {
                "name": course_name,
                "subj": subj,
                "ID": ID,
                "description": get_catalog_description(fields, course_name),
                "credits" : credit,
                "prerequisites": prereqs,
                "crosslisted": cross_listed,
                "offered": {
                    "year" : year,
                    "semesters" : semesters,
                    "text": offered_text
                },
                "properties": {
                    "CI": False,
                    "MR": False
                }
            }

    return data

def scrape_courses():
    print("Starting courses scraping")
    catalogs = get_catalogs()

    catalogs = catalogs[:2]
    courses_per_year = {}
    for index, (year, catalog_id) in enumerate(tqdm(catalogs)):
        course_ids = get_course_ids(catalog_id)
        data = get_course_data(course_ids, catalog_id)
        
        courses_per_year[year] = data
    # Serializing json
    json_object = json.dumps(courses_per_year, indent=4)
 
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
        print("Finished courses scraping")
    
    return courses_per_year

scrape_courses()