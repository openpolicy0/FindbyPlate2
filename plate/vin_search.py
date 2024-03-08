import requests
import sys
import os
import time

from tqdm import tqdm
from rich import print
from bs4 import BeautifulSoup
from time import sleep

def vin():
    pwd = os.getcwd()
    with open(pwd+"/plate/vin", "r") as v:
         vin = v.readline()

    url = 'https://www.vinfreecheck.com/vin/'+vin+'/vehicle-specification'

    r = requests.get(url)
    html = BeautifulSoup(r.text, "html.parser")
    sleep(0.2)

    animation = "|/-\\"

    for i in range(200):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("[bold green]\nDone![/bold green]")
    time.sleep(4)
    tag1 = html.find(["p"], class_="h2 subtitle-2")
    print("[dim cyan][INFO][CAR NAME]====>[/dim cyan][bold white]"+tag1.string+"[/bold white]")

    tag2 = html.find_all(["td", "div"], class_="txt")
    for tag2 in tag2:
        print("[dim cyan][INFO]====>[/dim cyan][bold white]"+tag2.string+"[/bold white]")
        sleep(0.2)
