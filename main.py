import requests
import sys
import os
import time
import socket

from rich import print
from bs4 import BeautifulSoup
from time import sleep

import plate.plate_search as PLATE
import plate.vin_search as VIN

os.system('clear')

try:
    socket.create_connection(("www.google.com", 80), timeout=5)
    print("[bold green]connected[/bold green]")
    sleep(1)
    os.system('clear')
except OSError:
    print("[bold red]no connection[/bold red]")
    sleep(1)
    os.system('clear')

print("""[bold blue]
   __ _         _ _              _      _       ___ 
  / _(_)_ _  __| | |__ _  _ _ __| |__ _| |_ ___|_  )
 |  _| | ' \/ _` | '_ \ || | '_ \ / _` |  _/ -_)/ / 
 |_| |_|_||_\__,_|_.__/\_, | .__/_\__,_|\__\___/___|
                       |__/|_|                      

[/bold blue]""")
pwd = os.getcwd()
print("""[purple]
type "help" for more options in terminal
type "show" for input variables and "set" to set the value ex. set <value>

!do not type full name of the given state, just abbreviation!
[/purple]""")

help_banner = """
options
===========

set options          info
-------------        ------
set plate            set lisense plate ex. set plate
set state            set lisense plate state ex. set state
set vin              set vin number of lisense plate
states               list all states to add a state

show plate options   show lisense plate options
show vin options     show vin lookup options
show all             show all options you defind

run_plate            run search on plate and get information on it
run_vin              run vin lookup and see details about the owners car

delete               delete files with the data inside them
exit                 exit tool
"""

def menu():
    plate = ''
    state = ''
    vin = ''

    try:
        fbp = str(input("(findbyplate2): ")).strip()
    except:
        time.sleep(0.1)
        sys.exit()

    _exit = False

    while not _exit:
        if fbp=="help":
            print(help_banner)

        elif fbp=="set":
            print("""[*] type "set -v" for detail info""")
            print("""(plate,state,vin)""")

        elif fbp=="set -v":
            print("""
    set options              info
    -------------            ------
    set plate                set plate number of car ex. "YZW902"
    set state                set state were the car is from ex. "CA"
    set vin                  set vin number (vehicle identification number) of
                            plate number
            """)

        elif fbp=="set plate":
            plate = str(input("plate: ")).strip()
            print("==>", plate)

        elif fbp=="set state":
            state = str(input("state: ")).strip()
            print("==>", state)

        elif fbp=="set vin":
            vin = str(input("vin: ")).strip()
            print("==>", vin)

        elif fbp=="show":
            print("""[*] type "show -v" for detail info""")
            print("(plate options,vin options, show all)")

        elif fbp=="show -v":
            print("""
    show options               info
    --------------             ------
    show plate options         show lisense plate options
    show vin options           show vin lookup options
    show all                   show all options you defind
            """)

        elif fbp=="show plate options":
            try:
                print("==>", plate)
                print("==>", state)
            except:
                print("""
    [dark_orange]no plate options found
    <define the target <plate/state> with <set> command>[/dark_orange]
                """)

        elif fbp=="show vin options":
            try:
                print("==>", vin)
            except:
                print("""
    [dark_orange]no vin number options found
    <define the target <vin> with the <set> command>[/dark_orange]
                """)

        elif fbp=="show all":
            try:
                print("==>", plate)
            except:
                print("[dark_orange]==> <plate> not defind[/dark_orange]")
            try:
                print("==>", state)
            except:
                print("[dark_orange]==> <state> not defind[/dark_orange]")
            try:
                print("==>", vin)
            except:
                print("[dark_orange]==> <vin> not defind[/dark_orange]")

        elif fbp=="states":
            print("""
    options         states
    ---------       --------
    AL  		alabama
    AK  		alaska
    AZ  		arizona
    AR  		arkansas
    CA  		california
    CO  		colorado
    CT  		connecticut
    DE  		delaware
    DC  		district of columbia
    FL  		florida
    GA  		Georgia
    HI  		hawaii
    ID  		idaho
    IL  		illinois
    IN  		indiana
    IA  		iowa
    KS  		kansas
    KY  		kentucky
    LA  		louisiana
    ME  		maine
    MD  		maryland
    MA  		massachusetts
    MI  		michigan
    MN  		minnesota
    MS  		mississippi
    MO  		missouri
    MT  		montana
    NE  		nebraska
    NV  		nevada
    MH  		new hampshire
    NJ  		new jersey
    NM  		new mexico
    NY  		new york
    NC  		north carolina
    ND  		north dakota
    OH  		ohio
    OK  		oklahoma
    OR  		oregon
    PA  		pennsylvania
    PR  		puerto rico
    RI  		rhode island
    SC  		south carolina
    SD  		south dakota
    TN  		tennessee
    TX  		texas
    UT  		utah
    VT  		vermont
    VA  		virginia
    WA  		washington
    WV  		west virginia
    WI  		wisconsin
    WY  		wyoming
            """)
            

        elif fbp=="run_plate":
            try:
                PLATE.plate()
            except:
                print("[dark_orange]<type error> not all objects are defind[/dark_orange]")

        elif fbp=="run_vin":
            try:
                VIN.vin()
            except:
                print("[dark_orange]<type error> not all objects are defind[/dark_orange]")

        elif fbp=="run_all":
            try:
                PLATE.plate()
            except:
                print("[dark_orange]<type error> plate/state not defind[/dark_orange]")
            try:
                VIN.vin()
            except:
                print("[dark_orange]<type error> vin number not defind[/dark_orange]")

        elif fbp=="exit":
            sleep(1)
            sys.exit()

        else:
            print("[red]error! no command found[/red]")

menu()
