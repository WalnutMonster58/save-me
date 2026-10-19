import shutil
import os
from time import sleep
import webbrowser

username = os.getlogin()
appleName = 0

print(username)

while True:
    original = r'..\save-me\apple.jpg'
    target = r'\users\{}\Downloads\apple{}.jpg'.format(username, appleName)
    print('attempting copy')
    shutil.copyfile(original, target)
    appleName = appleName + 1
