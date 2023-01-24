import json
import re
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import datetime
import os
from degree_util import get_catalogs


sand = requests.get("https://sis.rpi.edu/rss/bwckschd.p_disp_detail_sched?term_in=202209&crn_in=55504")
soup = BeautifulSoup(sand.content, "html.parser")
print(soup)