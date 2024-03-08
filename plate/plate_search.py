import requests
import sys
import os
import time
import random

from tqdm import tqdm
from rich import print
from bs4 import BeautifulSoup
from time import sleep

def plate():
    pwd = os.getcwd()
    with open(pwd+"/plate/plate", "r") as lp:
         plate = lp.readline()

    with open(pwd+"/plate/state", "r") as st:
         state = st.readline()

    url2 = 'https://findbyplate.com/US/'+state+'/'+plate+'/'

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
    }

    rs = requests.get(url2, headers=headers)
    report = BeautifulSoup(rs.text, "html.parser")
    sleep(0.2)

    animation = "|/-\\"
    for i in range(200):
        time.sleep(0.1)
        sys.stdout.write("\r<searching> [PLATE] " + animation[i % len(animation)])
        sys.stdout.flush()

    print("[bold green]\r ✅[/bold green]")
    time.sleep(4)
    tag_plate = report.find_all(["div", "/div"], class_="cell" or "clearfix")
    try:
        for tag_plate in tag_plate:
            print("[dim cyan][INFO]====>[/dim cyan][bold white]"+tag_plate.string+"[/bold white]")
            sleep(0.2)
    except TypeError:
            print("")
