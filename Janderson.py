from itertools import count
import keyboard
import webbrowser
from time import sleep

counter = 0
resetNum = 0
counterLimit = 100

while True:
    keyboard.wait('j')
    while counter < counterLimit:
        counter = counter + 1
        keyboard.press_and_release('backspace')
        keyboard.write('I HATE JUSTIN!!!!!!!!!!!!!!!!!!!!!!!!!')
        keyboard.press_and_release('enter')
        sleep(.5)
    if counter >= counterLimit:
        counter = 0
        resetNum = resetNum + 1
        print('reset #' + str(resetNum))
