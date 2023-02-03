import json
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import datetime
import os
from degree_util import get_catalogs
from degree_util import root


'''
year_generator makes use of the get_catalogs function
from the degree_util file which gives a list of all years with catalog data.
from there it takes the most recent 4 years and cleans them up to then be used in the sis_scraper.
'''
def year_generator():
    catalog = get_catalogs()
    years = catalog[:4]
    yearList = []
    for pair in years:
        yearList.append(pair[0][-4:])
    finalList = []
    for year in yearList:
        finalList.append(str(year) + '01') 
        finalList.append(str(year) + '05')
        finalList.append(str(year) + '09')
    return finalList

    


'''
sis_scraper goes through a .json file of courses
and pulls their subject and ID in order to make a call to SIS for
course information. It then makes use of BeautifulSoup to grab the html of the website and parse it for
the professors of the course and if it is CI(communication intensive)
It stores this information and then updates the .json file of courses with it.
'''
def sis_scraper():
    filepath = root
    f = open(filepath + '/frontend/src/data/courses.json','r')   #Opens the .json file and stores it as a python object
    courseJson = json.load(f)
    f.close()
    years = year_generator()
    years.reverse()
    s = requests.Session()

    for course in tqdm(courseJson): #Iterates through every course
        instructorStorage = []
        CI = False
        for currYear in years: #For every course we iterate through every year and open the respective webpage
            page = "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse"
            webpage_response = s.get(page + '?term_in=' + currYear + '&subj_in=' + courseJson[course]["subject"] + '&crse_in=' + courseJson[course]["ID"] + '&schd_in=L')
            webpage = webpage_response.content
            soup = BeautifulSoup(webpage, "html.parser")

            if soup.find(text=re.compile("No classes were found")) == None: #If the class is not offered this text is displayed, so we only search for information if this isn't present
                times = soup.findAll("table", {
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
                #This allows us to clean the text up to find if it is Communication Intensive. If it is we set a boolean to True
                search = r"""<span class="fieldlabeltext">Attributes: </span>(.*?)\n<br/>"""
                attribute = re.search(search, str(soup))
                tmp = attribute.group(1).strip() if attribute != None else ""
                if 'Communication Intensive' in tmp:
                    CI= True
                link = link_grabber(s, soup)
                restrictedMajor = majorRestrictionChecker(s, link)
                


        #With all of the information gathered we put it into the python json object and then push it back
        #into the course json
        instructorStorage = [*set(instructorStorage)]
        courseJson[course]['professors'] = instructorStorage
        courseJson[course]['properties']['CI'] = CI
        if len(restrictedMajor) > 0:
            courseJson[course]['properties']['MR'] = True
            courseJson[course]['properties']['majorRestriction'] = restrictedMajor
        else:
            courseJson[course]['properties']['MR'] = False
            courseJson[course]['properties']['majorRestriction'] = []
        f2 = open(filepath + '/frontend/src/data/courses.json', 'w')
        json.dump(courseJson, f2, sort_keys=True, indent=2, ensure_ascii=False)
        f2.close()



'''
link grabber takes in a given SIS page soup and finds the first class info
link in it and returns that link.
'''
def link_grabber(session, soup):
    link = ""
    key = "/rss/bwckschd.p_disp_detail_sched?term_in="
    linkMass = soup.find_all("a", href=True)
    for val in linkMass:
        if key in val['href']:
            link = val['href']
            break
    return link

'''
majorRestrictionChecker takes in a link and
turns it into an array of text lines.
From that it checks for a keyphrase and then returns 
text that is guaranteed to follow that keyphrase being the restricted majors.
If the keyphrase doesn't exist it returns an empty string.
'''
def majorRestrictionChecker(session, link):
    innerPage = "https://sis.rpi.edu" + link
    response = session.get(innerPage)
    innerContent = response.text
    soup2 = BeautifulSoup(innerContent, "html.parser")
    innerText = soup2.text
    textList = innerText.splitlines()
    red = list(filter(lambda item: item.strip(), textList))
    searchString = "Must be enrolled in one of the following Majors:"
    holder = []
    startingIndex = 0
    for i in range(0, len(textList) - 2):
        if searchString in textList[i]:
            startingIndex = i
            break
    dangerStringOne = "Return"
    dangerStringTwo = "Prerequisites"
    if startingIndex != 0:
        for j in range(startingIndex + 1, len(textList) - 1):
            if dangerStringOne in textList[j] or dangerStringTwo in textList[j]:
                break
            else:
                holder.append(textList[j].strip())
    majorList = list(filter(lambda item: item.strip(), holder))
    return majorList



    

    
    



            
if __name__ == '__main__':
    sis_scraper()


