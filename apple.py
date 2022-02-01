import shutil
from time import sleep
import webbrowser


appleName = 0

def appleopener():
    webbrowser.open('appleopener.py')

appleopener()

while True:
    original = r'..\save-me\apple.jpg'
    target = r'..\save-me\appleTest\apple{}.jpg'.format(appleName)
    print('attempting copy')
    shutil.copyfile(original, target)
    appleName = appleName + 1
