import keyboard
import webbrowser
import random
from time import sleep

word = str(input('what word would you like?'))
times = int(input('how many times?'))

for x in range(times + 1):
    x = str(x)
    if x == '1':
        print(x + ' ' + word)
    else:
        print(x + ' ' + word + 's')
