import keyboard
import webbrowser
import random
from time import sleep

#typer

print("Hi!")

counter = 0

while True:
    keyboard.wait('h')
    keyboard.wait('i')
    while True:
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('backspace')
        keyboard.write('HI!!!!!!!!')
        keyboard.press('enter')
        keyboard.release('enter')
        sleep(.5)
