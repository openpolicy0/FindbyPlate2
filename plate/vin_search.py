import requests
import sys
import os
import time

from tqdm import tqdm
from rich import print
from bs4 import BeautifulSoup
from time import sleep

def vin():
    with open("vin", "r") as v:
         vin = v.readline()

    url = 'https://www.vinfreecheck.com/vin/'+vin+'/vehicle-specification'

    r = requests.get(url)
    html = BeautifulSoup(r.text, "html.parser")
    sleep(0.2)
    for _ in tqdm(range(100),

        desc = "loading report...",
        ascii = False,ncols=100):
        time.sleep(0.1)
    time.sleep(1)
    print("[bold green]results found![/bold green]")
    sleep(4)
    tag1 = html.find(["p"], class_="h2 subtitle-2")
    print("[bold blue]=========================================================[/bold blue]")
    print("[dim cyan][INFO]====>[/dim cyan][bold white]"+tag1.string+"[/bold white]")

    tag2 = html.find_all(["td", "div"], class_="txt")
    for tag2 in tag2:
        print("[bold blue]=========================================================[/bold blue]")
        print("[dim cyan][INFO]====>[/dim cyan][bold white]"+tag2.string+"[/bold white]")
        sleep(1)
    print("[bold blue]=========================================================[/bold blue]")
