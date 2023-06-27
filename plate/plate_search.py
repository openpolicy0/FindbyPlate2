import requests
import sys
import os
import time

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
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-T220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    rs = requests.get(url2, headers=headers)
    report = BeautifulSoup(rs.text, "html.parser")
    sleep(0.2)
    for _ in tqdm(range(100),

       desc = "loading report...",
       ascii = False,ncols=100):
       time.sleep(0.1)
    time.sleep(1)
    print("[bold green]results found![/bold green]")
    time.sleep(4)
    tag_plate = report.find_all(["div", "/div"], class_="cell" or "clearfix")
    try:
        for tag_plate in tag_plate:
            print("[bold blue]=============================================================================[/bold blue]")
            print("[dim cyan][INFO]====>[/dim cyan][bold white]"+tag_plate.string+"[/bold white]")
            sleep(1)
        print("[bold blue]=============================================================================[/bold blue]")
    except TypeError:
            print("")
