import json
import os
filepath = os.path.dirname(os.getcwd())
# Opens the Department.JSON and returns a list of department code
def get_depts():
    depts = []
    f = open(filepath + '/data/depts.json', 'r') #make sure to close at end of file
    f = json.load(f)
    for dept in f:
        depts.append(dept)
    return depts

depts = get_depts()

def get_courses():
    f = open(filepath + '/data/courses.json','r')
    return json.load(f)

course_dict = get_courses()

def clean_list(s: str) -> str:
    return "".join([x for x in s if x.isalnum() or x.isspace()])