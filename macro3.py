import keyboard
import webbrowser
from time import sleep

counter = 0

keyboard.wait("C")

while counter <= 10:
    keyboard.press_and_release("left click")
    counter = counter + 1
    sleep(0.33)
