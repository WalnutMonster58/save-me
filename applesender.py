import keyboard
import webbrowser
import random
from time import sleep

#typer

print("Apple time?")

counter = 0

while True:
    keyboard.wait('a')
    keyboard.wait('p')
    keyboard.wait('p')
    keyboard.wait('l')
    keyboard.wait('e')
    while counter <= 100:
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('backspace')
        keyboard.write('https://youtu.be/g8EfOg7qK3M')
        keyboard.press_and_release('enter')
        counter = counter + 1
        sleep(.5)
    if counter >= 100:
        counter = 0
        print("reset")
