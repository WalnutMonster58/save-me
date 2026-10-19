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
            webbrowser.open('https://dehraflicks.com/wp-content/uploads/2025/12/troll-face-png.png')
            counter = counter + 1
            print('Trolled!')
        if counter >= 10:
            counter = 0
            bootlegTimer = random.randint(1,10)
