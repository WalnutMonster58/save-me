import keyboard
import webbrowser
from time import sleep

counter = 0
timer = 0

while True:
    keyboard.wait('shift+p')
    print("Let's Roll")
    while counter == 0:
        keyboard.write("ush yourself, because no one else is going to do it for you.Failure is the condiment that gives success its flavor.Wake up with determination. Go to bed with satisfaction.It's going to be hard, but hard does not mean impossible.Learning never exhausts the mind.The only way to do great work is to love what you do.")
        counter = counter + 1
    while counter != 0:
        keyboard.write("Push yourself, because no one else is going to do it for you.Failure is the condiment that gives success its flavor.Wake up with determination. Go to bed with satisfaction.It's going to be hard, but hard does not mean impossible.Learning never exhausts the mind.The only way to do great work is to love what you do.")
        sleep(.14)
