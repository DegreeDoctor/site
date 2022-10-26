import json
import aiohttp
import re
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests

async def get_details():

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=5)) as session:
        async with session.post(
                "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse",
                data = "term_in=202301&subj_in=MATH&crse_in=4800&schd_in=L" 
        )as request:
            html = await request.text()

    soup = BeautifulSoup(html, 'lxml-xml')
    return soup




def pog_scraper():
    f = open('courses.json','r')
    f1 = json.load(f)
    for course in f1:
        year = "202301"
        page = "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse"
        webpage_response = requests.get(page + '?term_in=' + year + '&subj_in=' + f1[course]["subj"] + '&crse_in=' + f1[course]["ID"] + '&schd_in=L')
        webpage = webpage_response.content
        soup = BeautifulSoup(webpage, "html.parser")
        
       

if __name__ == "__main__":
    year = "202209"
    page = "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse"
    webpage_response = requests.get(page + '?term_in=' + year + '&subj_in=' + "CSCI" + '&crse_in=' + "1100" + '&schd_in=L')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    print(soup)

