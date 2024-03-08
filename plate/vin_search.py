import requests
import sys
import os
import time

from googlesearch import search
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
    print()
    print("[dim cyan][INFO]====>[/dim cyan][bold white]searching vin number "+vin+" on google[/bold white]")
    print("[dim cyan][INFO]====>[/dim cyan][bold white]default search results set to <10>[/bold white]")
    animation = "|/-\\"

    for i in range(200):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("[bold green]\nDone![/bold green]")
    time.sleep(4)
    query = vin
    for url in search(query, num=10, stop=10, pause=2):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').get_text()
            print("""
[dim cyan][LINK]===> [/dim cyan][bold white]"""+url+"""[/bold white]
[dim cyan][TITLE][/dim cyan][bold white] """+title+"""[/bold white]
            """)
        except Exception as e:
            print("[bold red][ERROR][/bold red]:", e)
    print("""
[dim cyan][INFO]====> [/dim cyan][bold white]searching for """+tag1.string+""" in google[/bold white]
[dim cyan][INFO]====> [/dim cyan][bold white]default search results set to <10>[/bold white]
    """)

    query = tag1.string

    animation = "|/-\\"

    for i in range(200):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("[bold green]\nDone![/bold green]")
    time.sleep(4)
    for url in search(query, num=10, stop=10, pause=2):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').get_text()
            print("""
[dim cyan][LINK]===> [/dim cyan][bold white]"""+url+"""[/bold white]
[dim cyan][TITLE][/dim cyan][bold white] """+title+"""[/bold white]
            """)
            print()
        except:
            print("[bold red][ERROR][/bold red]: [bold white]timeout error[/bold white]")
