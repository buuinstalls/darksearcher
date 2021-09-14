##########################
# Fake dweb-search;      #
# By buu#1662 on discord #
##########################
# jajajaja
# ur bad kid

# Importing ]

import time
import os
import colorama
import webbrowser as wb
import random

# Variables ]

normal = "\u001b[0m"

red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
purple = "\u001b[35m"
cyan = "\u001b[36m"

# Function

def cprint(string):
    print(yellow + "[:] " + normal + string)
# ---------------------------------------------
def scprint(string):
    print(yellow + "    [:] " + normal + string)
# ---------------------------------------------
def cerror(string):
    print(red + "[#] " + normal + string)
# ---------------------------------------------
def scerror(string):
    print(red + "    [#] " + normal + string)
# ---------------------------------------------
def cinfo(string):
    print(blue + "[?] " + normal + string)
# ---------------------------------------------
def scinfo(string):
    print(blue + "    [?] " + normal + string)
# ---------------------------------------------
def cnotice(string):
    print(green + "[!] " + normal + string)
# ---------------------------------------------
def scnotice(string):
    print(green + "    [!] " + normal + string)
# ---------------------------------------------
def wprint(string):
    time.sleep(.02)
    print(yellow + "[:] " + normal + string)
# ---------------------------------------------
def swprint(string):
    time.sleep(.02)
    print(yellow + "    [:] " + normal + string)
# ---------------------------------------------
def cls():
    os.system("cls")
# ---------------------------------------------
def wait(string): # lol just in case i get mixed up with lua
    time.sleep(string)

# trollage

os.system("cls")

print(red + '''

 █▀▄ ▄▀█ █▀█ █▄▀ █▀ █▀▀ ▄▀█ █▀█ █▀▀ █░█
 █▄▀ █▀█ █▀▄ █░█ ▄█ ██▄ █▀█ █▀▄ █▄▄ █▀█
 ''')

lastnames = ["Hutchinson", "Mejia", "Lambert", "Gonzalez", "Davis", "Mcgrath", "Valentine", "Mosley", "Rivers", "Summers", "Leonard", "Benton", "Dominguez", "Henson", "Rivas", "Griffin", "Cohen", "Espinoza", "Dillon", "Walton", "Clark", "Lucas", "Byrd", "Frank", "Shannon", "Leblanc", "Cox", "Rivas", "Villarreal", "Reese", "Kirk", "Guerrero", "Hester", "Tanner", "Reilly", "Clayton"]

name = input("Enter your name : ")
cinfo(f"Searching for the name {red} {name} {normal};")
time.sleep(1)
cinfo("Multiple Names Found.")
cerror("Listing.")
time.sleep(.5)
if name.lower() == "ruddy":
    print(f"{name} ['Villar-Martinez']")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
elif name.lower() == "hendrick":
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} ['Xavier']")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
elif name.lower() == "david":
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} ['Mantilla']")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
elif name.lower() == "christian":
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} ['Arce-Escobar']")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
elif name.lower() == "brianna":
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} ['Duque']")
elif name.lower() == "jayden":
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} ['Leveille']")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
else:
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")
    print(f"{name} {random.choices(lastnames)}")

cinfo("Process Finished.")

time.sleep(999)