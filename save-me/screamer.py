from playsound import playsound
from time import sleep

while True:
    vals = 1

    
    for x in range(vals + 1):
        sleep(1)
        print(x)
        
        if x == vals:
            print('SCREAM!!!!!!!!!!!!!!!!!!!!!!!!')            
            playsound('audio/scream.mp3', block=True)
    