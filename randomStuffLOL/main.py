import pyttsx3
from random import randint
from time import sleep
from playsound import playsound


engine = pyttsx3.init()

rng = 0 

while True:
    
    rng = randint(1,10)
    print(rng)


    if rng == 10:
        engine.say('sigh...')
        sleep(1)
        numTimes = randint(1,1000)
        print(numTimes)
        for x in range(numTimes):
            playsound('audio/lol.mp3', block=sleep(.2))
        rng = 0

    sleep(1)
