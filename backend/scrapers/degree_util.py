import json
import os
import unicodedata

# uniform filepath for all backend routing
filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Opens the subjects.JSON and returns a list of subject code
def get_subjs():
    subjs = []
    f = open(filepath + '/data/subjs.json', 'r') #make sure to close at end of file
    tmp = json.load(f)
    for subj in tmp:
        subjs.append(subj)
    f.close()
    return subjs

subjs = get_subjs()

def get_courses():
    f = open(filepath + '/data/courses.json','r')
    ret = json.load(f)
    f.close()
    return ret

course_dict = get_courses()

def get_prgms():
    prgms = []
    f = open(filepath + '/data/skip_prgms.json', 'r')
    tmp = json.load(f)
    for prgm in tmp:
        prgms.append(prgm)
    f.close()
    return prgms

prgms = get_prgms()


# QOL functions 
def clean_str(s: str) -> str:
    return "".join([x for x in s if x.isalnum() or x.isspace()])

def rep_uni(str):
    return str.replace("\n","").replace("\t","").replace("\u200b","").replace("\u2013","").replace("\u00ad","")

# Normalize a string, using unicode data. Remove all weird whitespace tag 
def norm_str(str):
    s1 = unicodedata.normalize("NFKD",str).strip()
    return rep_uni(s1)

# Take a list of list and remove empty list elements
def striplist(lstr): 
    return list(filter(None, lstr))