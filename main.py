import requests
import sys
import os
import time
import socket
import json

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

with open('states.json', 'r') as f:
    states = json.load(f)

def plate_set(plate):
    return len(plate) > 1

def state_set(state):
    return len(state) > 1

def vin_set(vin):
    return len(vin) > 1

def menu():
    plate = ''
    state = ''
    vin = ''

    _exit = False

    while not _exit:
        try:
            fbp = str(input("(findbyplate2): ")).strip()
        except KeyboardInterrupt:
            print('Exiting...')
            exit()
            
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
            if not plate_set(plate) or not state_set(state):
                print("""
    [dark_orange]no plate options found
    <define the target <plate/state> with <set> command>[/dark_orange]
                """)
                return

            print("==>", plate)
            print("==>", state)

        elif fbp=="show vin options":
            if not vin_set(vin):
                print("""
    [dark_orange]no vin number options found
    <define the target <vin> with the <set> command>[/dark_orange]
                """)
                return

            print("==>", vin)
                

        elif fbp=="show all":
            if plate_set(plate):
                print("==>", plate)
            if state_set(state):
                print("==>", state)
            if vin_set(vin):
                print("==>", vin)

        elif fbp=="states":
            print("""
options         states
---------       --------""")
            for abbreviation, name in states.items():
                print(f"{abbreviation}\t\t{name}")

        elif fbp=="run_plate":
            if not plate_set(plate):
                print("No plate set.")
                return

            PLATE.search_plate(plate, state)

        elif fbp=="run_vin":
            if not vin_set(vin):
                print("No VIN set.")
                return

            VIN.search_vin(vin)

        elif fbp=="run_all":
            if not plate_set(plate):
                print("No plate set.")
                return
            
            PLATE.search_plate(plate, state)
            
            if not vin_set(vin):
                print("No VIN set.")
                return

            VIN.search_vin(vin)

        elif fbp=="exit":
            sleep(1)
            sys.exit()

        else:
            print("[red]error! no command found[/red]")

menu()
