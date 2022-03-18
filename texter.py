import keyboard
import webbrowser
import random
from time import sleep

#typer

print("Stop annoying me!")

words = ['k', 'lol', 'lmao', 'cool', 'epic', 'awesome!', 'deez nuts', 'mug is better', 'i love the fbi', 'i smell you', 'among us', 'adopt a random child', 'will', 'john', 'jaysin', 'eddie', 'quinn', 'callum', 'christan', 'dont care', 'no bitches?']

counter = 0

while True:
    keyboard.wait('0')
    while counter <= 10:
        text = random.randint(0,len(words) - 1)
        keyboard.press_and_release('backspace')
        keyboard.write(words[text])
        keyboard.press('enter')
        keyboard.release('enter')
        counter = counter + 1
        sleep(1)
    if counter >= 10:
        counter = 0
        print("reset")
