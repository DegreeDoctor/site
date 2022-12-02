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
        #return soup
        table = soup.find('table', class_='datadisplaytable')
        linkMass = table.find_all("a", href=True)
        sexyLinkList = []
        key = "/rss/bwckctlg.p_disp_course_detail?cat_term_in="
        for val in linkMass:
            if key in val['href']:
                link = val['href']
                sexyLinkList.append("https://sis.rpi.edu" + link)
        for link in sexyLinkList:
            sexy = s.get(link)
            sexyContent = sexy.content
            sexySoup = BeautifulSoup(sexyContent, "html.parser")
            return soup

        
        #for course in soup.find_all("td", class_="nttitle"):
            #print(course)

            #courseCode = course.find("td", class_="dddefault").text

if __name__ == '__main__':
    sand = deep_sis_scraper()
    print(sand)