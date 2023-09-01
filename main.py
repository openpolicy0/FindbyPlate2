import requests
import sys
import os
import time

from rich import print
from bs4 import BeautifulSoup
from time import sleep

import plate.plate_search as PLATE
import plate.vin_search as VIN

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
[/purple]""")

def menu():
    try:
        fbp = str(input("(findbyplate2) ")).strip()
    except:
        time.sleep(0.1)
        sys.exit()

    if fbp=="help":
       print("""
  options
===========

 set options      info
-------------    ------
set plate         set lisense plate ex. set plate
set state         set lisense plate state ex. set state
set vin           set vin number of lisense plate
list states       list all states to add a state

show plate-options      show lisense plate options
show vin-options        show vin lookup options

run plate-search  run search on plate and get information on it
run vin-search    run vin lookup and see details about the owners car

       """)
       menu()

    elif fbp=="set plate":
         global plate
         plate = str(input("plate: ")).strip()
         print("==>", plate)
         with open(pwd+"/plate/plate", "w") as f:
              f.write(plate)
         menu()

    elif fbp=="set state":
         global state
         state = str(input("state: ")).strip()
         print("==>", state)
         with open(pwd+"/plate/state", "w") as f:
              f.write(state)
         menu()

    elif fbp=="set vin":
         global vin
         vin = str(input("vin: ")).strip()
         print("==>", vin)
         with open(pwd+"/plate/vin", "w") as f:
              f.write(vin)
         menu()

    elif fbp=="":
         menu()

    elif fbp=="show":
         print("""[*] type "show -v" for detail info""")
         print("(plate-options,vin-options)")
         menu()

    elif fbp=="show -v":
         print("""
 show options               info
--------------             ------
show plate-options         show lisense plate options
show vin-options           show vin lookup options
         """)
         menu()

    elif fbp=="show plate-options":
         try:
             print("==>", plate)
             print("==>", state)
         except:
             print("[dark_orange]no plate options found[/dark_orange]")
         menu()

    elif fbp=="show vin-options":
         try:
             print("==>", vin)
         except:
             print("[dark_orange]no vin number options found[/dark_orange]")
         menu()

    elif fbp=="list states":
         print("""[blue]
AL - alabama
AK - alaska
AZ - arizona
AR - arkansas
CA - california
CO - colorado
CT - connecticut
DE - delaware
DC - district of columbia
FL - florida
GA - Georgia
HI - hawaii
ID - idaho
IL - illinois
IN - indiana
IA - iowa
KS - kansas
KY - kentucky
LA - louisiana
ME - maine
MD - maryland
MA - massachusetts
MI - michigan
MN - minnesota
MS - mississippi
MO - missouri
MT - montana
NE - nebraska
NV - nevada
MH - new hampshire
NJ - new jersey
NM - new mexico
NY - new york
NC - north carolina
ND - north dakota
OH - ohio
OK - oklahoma
OR - oregon
PA - pennsylvania
PR - puerto rico
RI - rhode island
SC - south carolina
SD - south dakota
TN - tennessee
TX - texas
UT - utah
VT - vermont
VA - virginia
WA - washington
WV - west virginia
WI - wisconsin
WY - wyoming
         [/blue]""")
         menu()

    elif fbp=="run plate-search":
         try:
             PLATE.plate()
         except:
             print("[dark_orange]<type error> not all objects are defind[/dark_orange]")
         menu()

    elif fbp=="run vin-search":
         try:
             VIN.vin()
         except:
             print("[dark_orange]<type error> not all objects are defind[/dark_orange]")
         menu()

    else:
        print("[red]error! no command found[/red]")
        menu()

menu()
