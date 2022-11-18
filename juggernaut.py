import subprocess
import time
import keyboard
from time import sleep

outlook = 'juggernaut.py'
active = False
while True:
    if keyboard.is_pressed('b'):
        print("b has been pressed")
        active = True
        sleep(1)
        
    while active == True:
        if keyboard.is_pressed('b'):
            print("b has been pressed")
            active = False
            sleep(1)
            
        p = subprocess.Popen(outlook)
        p.wait()  # just wait for the child to end and... restart it immediately
        time.sleep(5)   # unsure if really useful
        print("currently active")
        sleep(1)