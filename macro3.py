import pyautogui
import keyboard
from time import sleep

counter = 0

keyboard.wait('c')

while counter <= 10:
    pyautogui.click(100, 100)
    print(counter)
    sleep(1)
    counter = counter + 1

    if counter > 10:
        counter = 0
