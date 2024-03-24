import requests
import sys
import time
import random
import re

from tqdm import tqdm
from rich import print
from bs4 import BeautifulSoup
from time import sleep

def search_plate(plate, state):
    url2 = 'https://findbyplate.com/US/'+state.upper()+'/'+plate.upper()+'/'

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
    car = report.find(["h2"], class_="vehicle-modal")
    place = report.find(["a"], href="https://findbyplate.com/US/")
    location = report.find(["a"], href="https://findbyplate.com/US/"+state.upper()+"/")
    info = report.find(["p"], style="text-align:left;")
    pl = place.string
    lo = location.string
    print("[dim cyan][INFO][CAR NAME]====>[/dim cyan] [bold white] "+car.string+"[/bold white]")
    sleep(0.2)
    print("|_", lo)
    sleep(0.2)
    print("  |_", pl)
    sleep(0.2)
    print("[dim cyan][DETAILS]====>[/dim cyan] [bold white]"+info.string+"[/bold white]")
    try:
        count = 0
        for tag_plate in tag_plate:
            print("[dim cyan][INFO]====>[/dim cyan][bold white]"+tag_plate.string+"[/bold white]")
            count += 1
            sleep(0.2)
    except TypeError:
            print("")
    print("we found", count, "results for", plate.upper())
    print("[dim cyan][IMAGE][/dim cyan] https://cdn.findbyplate.com/US/"+state.upper()+"/"+plate.upper()+".jpg")
