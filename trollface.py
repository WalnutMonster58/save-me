import tkinter
import os
import webbrowser
from time import sleep
import random


counter = 0

while True:
    bootlegTimer = random.randint(1,100)
    print(bootlegTimer)
    sleep(1)
    while bootlegTimer == 10:
        bootlegTimer == 10
        if counter < 10:
            webbrowser.open('https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/220px-Trollface_non-free.png')
            counter = counter + 1
            print('Trolled!')
        if counter >= 10:
            counter = 0
            bootlegTimer = random.randint(1,10)
