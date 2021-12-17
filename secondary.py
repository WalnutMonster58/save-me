import tkinter
import os
import webbrowser
from time import sleep
import random


while True:
    counter = random.randint(1,10)
    sleep(1)
    if counter == 5:
        webbrowser.open('https://www.youtube.com/channel/UC1rHmb-Euu1R0HsVFah3VtQ')
