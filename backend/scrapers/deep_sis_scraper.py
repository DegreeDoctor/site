import json
from bs4 import BeautifulSoup
import requests
import os
from degree_util import get_subjs
import numpy as np




def tailGenerator(subjectList):
    tails = []
    for subject in subjectList:
        tails.append("&sel_subj=" + subject)
    kachow = np.array_split(tails, 15)
    return kachow

def deep_sis_scraper():
    filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    f = open(filepath + '/data/courses.json','r')   #Opens the .json file and stores it as a python object
    courseJson = json.load(f)
    f.close()
    s = requests.Session()
    head = "https://sis.rpi.edu/rss/bwckctlg.p_display_courses?term_in=202209&call_proc_in=&sel_subj=&sel_levl=&sel_schd=&sel_coll=&sel_divs=&sel_dept=&sel_attr="
    subjectList = get_subjs()
    tail = ""
    tail = tailGenerator(subjectList)
    urlTails = []
    for list in tail:
        urlTails.append(''.join(list))
    for tails in urlTails:
        webpage_response = s.get(head + tails)
        webpage = webpage_response.content
        soup = BeautifulSoup(webpage, "html.parser")
        table = soup.find('table', class_='datadisplaytable')
        linkMass = table.find_all("a", href=True)
        allLinks = []
        key = "/rss/bwckctlg.p_disp_course_detail?cat_term_in="
        for val in linkMass:
            if key in val['href']:
                link = val['href']
                allLinks.append("https://sis.rpi.edu" + link)
        for link in allLinks:
            #link = "https://sis.rpi.edu/rss/bwckctlg.p_disp_course_detail?cat_term_in=202209&subj_code_in=BIOL&crse_numb_in=4310"
            Lcontent = s.get(link)
            deepContent = Lcontent.content
            contentSoup = BeautifulSoup(deepContent, "html.parser")
            classInformation = contentSoup.text
            classText = classInformation.splitlines()
            while("" in classText):
                classText.remove("")
            subjectIndex =  link.find("subj_code_in=")
            subject = ""
            for i in range(subjectIndex + 13, len(link)):
                if link[i] == "&":
                    break
                subject += link[i]
            #SUBJECT IS NOW FETCHED CORRECTLY--------------------------------
            courseIndex =  int(link.find("crse_numb_in="))
            courseID = link[courseIndex + 13:int(len(link))]

            #checking if the course starts with 6 or 9, those are illegal classes
            if courseID[0] == "6" or courseID[0] == "9":
                continue
            #COURSEID IS NOW FETCHED CORRECTLY---------------------------------
            courseInfo = ""
            courseInfoIndex = 0
            for i in range(0, len(classText)):
                if subject in classText[i]:
                    courseInfo = classText[i]
                    courseInfoIndex = i
                    break
            IDindex = courseInfo.find(courseID) + 7
            courseName = courseInfo[IDindex:]

            #checking if the course is an elective, if it is, we don't want it
            if "elective" in courseName.lower():
                continue
            #COURSE NAME IS NOW FETCHED CORRECTLY----------------------------
            courseDescription = ""
            descriptionIndex = courseInfoIndex + 1
            if classText[descriptionIndex].strip()[0].isdigit():
                continue
            else:
                courseDescription = classText[descriptionIndex].strip()
            #courseDescription IS NOW FETCHED CORRECTLY----------------------
            for i in range(0, len(classText)):
                if "credit hours" in classText[i].lower():
                    creditIndex = i
                    break
            creditHours = classText[creditIndex].split(" ")[0]
            #creditHours IS NOW FETCHED CORRECTLY----------------------------


            
            


            


        
    

if __name__ == '__main__':
    sand = deep_sis_scraper()
    print(sand)