from time import sleep
import keyboard
import random
import threading

chance = 0
countdown = 5

while True:
    if countdown > 0:
        print(countdown)
        countdown = countdown - 1
        sleep(1)
    if countdown == 0:
        print("Random Time")
        countdown = countdown - 1
    if countdown < 0:
        chance = random.randint(1,11)
        if chance in range(1,3):
            print("Right")
            keyboard.press("d")
            sleep(.5)
            keyboard.release("d")
        if chance in range(4,5):
            print("Jump")
            keyboard.press_and_release("spacebar")
        if chance == 6:
            print("Left")
            keyboard.press("a")
            sleep(.5)
            keyboard.release("a")
        if chance == 7:
            keyboard.press_and_release("s")
            print("Down")
        if chance == 8:
            print("up")
            keyboard.press_and_release("w")
        if chance in range(9,10):
            print("Right Jump")
            keyboard.press_and_release("spacebar")
            keyboard.press("d")
            sleep(.5)
            keyboard.release("d")
            if chance == 11:
                print("Left Jump")
                keyboard.press_and_release("spacebar")
                keyboard.press("a")
                sleep(.5)
                keyboard.release("a")


        sleep(.5)
