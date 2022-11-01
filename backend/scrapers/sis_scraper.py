import json
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import datetime
import os


'''
year_generator uses the datetime library to grab the current year.
With this it creates a list of the past 4 years, including the current year.
Finally, it creates a new list of each of the aforementioned years including the semester call codes for
SIS calls.
'''
def year_generator():
    currYear = (datetime.date.today()).year  
    yearList = list(range(currYear - 3, currYear + 1))
    finalList = []
    for year in yearList:
        finalList.append(str(year) + '09') #Fall
        finalList.append(str(year) + '01') #Spring
        finalList.append(str(year) + '05') #Arch
    return finalList



'''
sis_scraper goes through a .json file of courses
and pulls their subject and ID in order to make a call to SIS for
course information. It then makes use of BeautifulSoup to grab the html of the website and parse it for
the professors of the course and if it is CI(communication intensive)
It stores this information and then updates the .json file of courses with it.
'''
def sis_scraper():
    filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    f = open(filepath + '/data/courses.json','r')   #Opens the .json file and stores it as a python object
    courseJson = json.load(f)
    f.close()

    for course in tqdm(courseJson): #Iterates through every course
        instructorStorage = []
        CI = False
        years = year_generator()

        for currYear in years: #For every course we iterate through every year and open the respective webpage
            page = "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse"
            webpage_response = requests.get(page + '?term_in=' + currYear + '&subj_in=' + courseJson[course]["subj"] + '&crse_in=' + courseJson[course]["ID"] + '&schd_in=L')
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

        #With all of the information gathered we put it into the python json object and then push it back
        #into the course json
        instructorStorage = [*set(instructorStorage)]
        courseJson[course]['professors'] = instructorStorage
        courseJson[course]['properties']['CI'] = CI
        f2 = open(filepath + '/data/courses.json', 'w')
        json.dump(courseJson, f2, sort_keys=True, indent=2, ensure_ascii=False)
        f2.close()
            
if __name__ == '__main__':
    sis_scraper()
        
       



