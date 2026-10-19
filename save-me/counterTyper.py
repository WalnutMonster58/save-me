import keyboard
from time import sleep

word = str(input('what word would you like?'))
times = int(input('how many times?'))

print('Click on line to write on within 5 seconds')
sleep(5)

for x in range(times + 1):
    x = str(x)

    if x != "0":
        if x == '1':
            keyboard.write(x + ' ' + word + ' ')
        else:
            keyboard.write(x + ' ' + word + 's ')
