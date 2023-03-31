import json
from bs4 import BeautifulSoup
import requests
import os
from degree_util import get_subjs
import numpy as np
from sis_scraper import year_generator
import re
from sis_scraper import link_grabber
from sis_scraper import majorRestrictionChecker
from tqdm import tqdm
from degree_util import root






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
    head = "https://sis.rpi.edu/rss/bwckctlg.p_display_courses?term_in=ZIGGSISTHEBEST&call_proc_in=&sel_subj=&sel_levl=&sel_schd=&sel_coll=&sel_divs=&sel_dept=&sel_attr="
    #ziggs is definitely the goat of all time 😈😈
    subjectList = get_subjs()
    tail = ""
    tail = tailGenerator(subjectList)
    urlTails = []
    years = year_generator()
    years.reverse()


    for list in tail:
        urlTails.append(''.join(list))
    for tails in tqdm(urlTails):
        for year in years:
            tempHead = head.replace("ZIGGSISTHEBEST", str(year))
            webpage_response = s.get(tempHead + tails)
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
                #link = "https://sis.rpi.edu/rss/bwckctlg.p_disp_course_detail?cat_term_in=202209&subj_code_in=COGS&crse_numb_in=2940"
                #link = "https://sis.rpi.edu/rss/bwckctlg.p_disp_course_detail?cat_term_in=202209&subj_code_in=CSCI&crse_numb_in=4480"
                #link = "https://sis.rpi.edu/rss/bwckctlg.p_disp_course_detail?cat_term_in=202209&subj_code_in=ASTR&crse_numb_in=4220"
                Lcontent = s.get(link)
                deepContent = Lcontent.content
                contentSoup = BeautifulSoup(deepContent, "html.parser")
                classInformation = contentSoup.text
                classText = classInformation.splitlines()
                while("" in classText):
                    classText.remove("")
                subjectIndex =  link.find("subj_code_in=")
                courseSubject = ""
                for i in range(subjectIndex + 13, len(link)):
                    if link[i] == "&":
                        break
                    courseSubject += link[i]
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
                    if courseSubject in classText[i]:
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
                creditFound = False
                if classText[descriptionIndex].strip()[0].isdigit():
                    creditFound = True
                else:
                    courseDescription = classText[descriptionIndex].strip()
                #courseDescription IS NOW FETCHED CORRECTLY----------------------
                creditStorage = ""
                classCredits = []
                if creditFound == False:

                    for i in range(0, len(classText)):
                        if "credit hours" in classText[i].lower():
                            creditIndex = i
                            break
                    creditStorage = classText[creditIndex]
                    for val in creditStorage:
                        if val.isdigit() and val!= "0":
                            classCredits.append(val)
                else:
                    creditStorage = classText[descriptionIndex].strip()
                if creditStorage != "":
                    for val in creditStorage:
                        if val.isdigit() and val != "0":
                            classCredits.append(val)
                cleanCredits = np.unique(classCredits)

                #creditHours IS NOW FETCHED CORRECTLY----------------------------

                #PREREQUISITES ARE NOW FETCHED CORRECTLY------------------------- HE SAYS XD
                searchString = "Cross Listed: "
                crossedIndex = 0
                for i in range(0, len(classText)):
                    if searchString in classText[i]:
                        crossedIndex = i
                        break
                crossListed = ""
                crossListing = ""
                if crossedIndex != 0:
                    crossListed = classText[i].find(searchString) + len(searchString)
                    crossListing = classText[i][crossListed:crossListed + 9]
                
                #crossListed IS NOW FETCHED CORRECTLY----------------------------


                search = r"""<span class="fieldlabeltext">Attributes: </span>(.*?)\n<br/>"""
                attribute = re.search(search, str(soup))
                tmp = attribute.group(1).strip() if attribute != None else ""
                if 'Communication Intensive' in tmp:
                    CI= True
                else:
                    CI = False
                #communication intensive is now fetched correctly--------------------------

                #major restriction
                link = "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse?term_in=" + year + "&subj_in=" + courseSubject +"&crse_in=" + courseID +"&schd_in=L"
                mrPage = s.get(link)
                mrContent = mrPage.content
                mrSoup = BeautifulSoup(mrContent, "html.parser")
                pogLink = link_grabber(s, mrSoup)
                restrictedMajor = majorRestrictionChecker(s, pogLink)
                #major restriction is now fetched correctly--------------------------


                #professors
                instructorStorage = []
                professorYear = year
                professorSubject = courseSubject
                professorID = courseID
                professorLink = "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse?term_in=" + professorYear + "&subj_in=" + professorSubject + "&crse_in=" + professorID + "&schd_in=L"
                professorWebPage = s.get(professorLink)
                professorContent = professorWebPage.content
                professorSoup = BeautifulSoup(professorContent, "html.parser")
                times = professorSoup.findAll("table", {
                    "class": "datadisplaytable",
                    "summary": "This table lists the scheduled meeting times and assigned instructors for this class..",
                })
                #This allows us to clean the text up to easily find the professors, and then we grab the professor names and place them into a list
                for time in times:
                    split_up = [x.text for x in time.findAll("td")]
                    instructor = split_up[6].split('(')[0]
                    instructor = re.sub(' +', ' ', instructor).strip()
                    if instructor != "TBA":
                        instructorStorage.append(instructor)
                cleanInstructors = np.unique(instructorStorage)
                #PROFESSORS ARE NOW FETCHED CORRECTLY----------------------------
                
                

                #when offered(deal with later)


                #hey guys its time for me to put you in the json >:)

                filepath = root
                f = open(filepath + '/frontend/src/data/courses.json','r')   #Opens the .json file and stores it as a python object
                courseJson = json.load(f)
                f.close()
                if(courseName not in courseJson):
                    courseJson[courseName] = {} #creates a new course in the json file
                    courseJson[courseName]['properties'] = {}
                
                courseJson[courseName]['subject'] = courseSubject #adds the subject to the course
                courseJson[courseName]['ID'] = courseID #adds the ID to the course
                courseJson[courseName]['description'] = courseDescription #adds the description to the course
                courseJson[courseName]['credits'] = cleanCredits.tolist() #adds the credits to the course
                #courseJson[courseName]#prereqs
                courseJson[courseName]['crosslisted'] = crossListing #adds the crossListing to the course
                courseJson[courseName]['properties']['CI'] = CI #adds if communication intensive to the course
                if len(restrictedMajor) > 0:
                    courseJson[courseName]['properties']['MR'] = True
                    courseJson[courseName]['properties']['majorRestriction'] = restrictedMajor
                else:
                    courseJson[courseName]['properties']['MR'] = False
                    courseJson[courseName]['properties']['majorRestriction'] = []
                courseJson[courseName]['professors'] = cleanInstructors.tolist() #adds the professors to the course
                #when offered


                f2 = open(filepath + '/frontend/src/data/courses.json', 'w')
                json.dump(courseJson, f2, sort_keys=True, indent=2, ensure_ascii=False)
                f2.close()



            


                        
                
            
            


            


        
    

if __name__ == '__main__':
    sand = deep_sis_scraper()
    print(sand)