import tkinter
import os
import webbrowser
from time import sleep
import random


while True:
    counter = random.randint(1,100)
    sleep(1)
    print(counter)
    if counter == 50:
        webbrowser.open('https://www.youtube.com/channel/UC1rHmb-Euu1R0HsVFah3VtQ')
