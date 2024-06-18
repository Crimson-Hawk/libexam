#SPDX-FileCopyrightText: 2024 Crimson Hawk
#SPDX-License-Identifier: GPL-3.0-or-later
import base64
import hashlib
import string
import time
import keyboard
import os
from libexam.py import *


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If computer is running windows use cls
        command = 'cls'
    os.system(command)


print("""
         ___  ___  __
        /  / /__/ / /    Coded by Crimson Hawk
       /  / ___  / /___  ____  __  __     _____    __ __ __
      /  / /  / / __  / / _  / \\ \\/ /    / __  /  /  /  /  /
     /  / /  / / /_/ / / /__/  / /\\ \\   / /_/ /  /  /__/  /
    /__/ /__/ /_____/ /____/  /_/  \\_\\ /____/_/ /__/  /__/
    """)

print(f"libexam frontend UI initiated")

sleep(1)
print("\r")

libexam.setmode(1)  #setmode as client

username = ""

print(f"""
 ______________________________
|                              |
|   libexam demo frontend ui   |
|                              |
|  Username:{username}
|                              |
|           (L)ogin            |
|______________________________|""")

while (True):
    key = keyboard.wait()
    #print(f"{key} pressed")
    username = username + key
    clearConsole()
    print(f"""
 ______________________________
|                              |
|   libexam demo frontend ui   |
|                              |
|  Username:{username}
|                              |
|           (L)ogin            |
|______________________________|""")
