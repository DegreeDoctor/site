import json
import aiohttp
import re
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm

async def get_details():

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=5)) as session:
        async with session.post(
                "https://sis.rpi.edu/rss/bwckctlg.p_disp_listcrse",
                data = "term_in=202301&subj_in=MATH&crse_in=4800&schd_in=L" 
        )as request:
            html = await request.text()

    soup = BeautifulSoup(html, 'lxml-xml')
    return soup
       

if __name__ == "__main__":
    soup = asyncio.run(get_details())
    print(soup)