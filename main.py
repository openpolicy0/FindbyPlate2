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

go to "https://findbyplate.com" and lookup the lisnse plate, input the plate in your terminal
!do not type full name of the given state, just abbreviation! (ex. CA)
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

show options         show options PLATE, STATE, VIN

run_plate            run search on plate and get information on it
run_vin              run vin lookup and see details about the owners car
run_all              run all searches on the target (lisense plate)
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
            print('[dark_orange]\nExiting...[/dark_orange]')
            sleep(0.3)
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
            print("==>", plate.upper())

        elif fbp=="set state":
            state = str(input("state: ")).strip()
            print("==>", state.upper())

        elif fbp=="set vin":
            vin = str(input("vin: ")).strip()
            print("==>", vin.upper())

        elif fbp=="show":
            print("""[*] type "show options" for detail info""")

        elif fbp=="show options":
            print("""
  show options               info
 --------------             ------
 show options               show options PLATE, STATE,
                            VIN
            """)
            s = ' '
            if plate_set(plate):
                print(" PLATE",s*20, plate.upper())
            else:
               print(" PLATE",s*20, "N/A")
            if state_set(state):
                print("\n STATE",s*20, state.upper())
            else:
               print("\n STATE",s*20, "N/A")
            if vin_set(vin):
                print("\n VIN",s*22, vin.upper())
            else:
               print("\n VIN",s*22, "N/A")

        elif fbp=="states":
            print("""
options         states
---------       --------""")
            for abbreviation, name in states.items():
                print(f"{abbreviation}\t\t{name}")

        elif fbp=="run_plate":
            if not plate_set(plate):
                print("[bold blue][*][/bold blue] No plate set.")
                continue

            PLATE.search_plate(plate, state)

        elif fbp=="run_vin":
            if not vin_set(vin):
                print("[bold blue][*][/bold blue] No VIN set.")
                continue
                sleep(0.1)
            VIN.lookup_vin(vin)

        elif fbp=="run_all":
            if not plate_set(plate):
                print("[bold blue][*][/bold blue] No plate set.")
                continue
                sleep(0.1)
            PLATE.search_plate(plate, state)

            if not vin_set(vin):
                print("[bold blue][*][/bold blue] No VIN set.")
                continue
                sleep(0.1)
            VIN.lookup_vin(vin)

        elif fbp=="exit":
            sleep(1)
            sys.exit()

        elif fbp=="":
           menu()

        else:
            print("[bold red][*][/bold red] [bold white]no command "+fbp+" found[/bold white]")

menu()
