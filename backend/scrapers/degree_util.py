import json
import os
filepath = os.path.dirname(os.getcwd())
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

def clean_list(s: str) -> str:
    return "".join([x for x in s if x.isalnum() or x.isspace()])