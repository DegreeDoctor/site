import json

# Opens the Department.JSON and returns a list of department code
def get_depts():
    depts = []
    f = open('depts.json', 'r') #make sure to close at end of file
    f = json.load(f)
    for dept in f:
        depts.append(dept)
    return depts

depts = get_depts()

def get_courses():
    course_dict = []
    f = open('courses.json','r')
    f = json.load(f)
    for course in f:
        course_dict.append(course)
    return course_dict

course_dict = get_courses()