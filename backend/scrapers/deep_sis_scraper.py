import json
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import datetime
import os
from degree_util import get_subjs
from lxml import html
import numpy as np





def tailGenerator(subjectList):
    tails = []
    for subject in subjectList:
        tails.append("&sel_subj=" + subject)
    kachow = np.array_split(tails, 5)
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
    for list in tail:
        "".join(list)
    for tails in tail:
        webpage_response = s.get(head + tail)
        webpage = webpage_response.content
        soup = BeautifulSoup(webpage, "html.parser")
    


if __name__ == '__main__':
    sand = deep_sis_scraper()
    for val in sand:
        print(val)
        print("")
