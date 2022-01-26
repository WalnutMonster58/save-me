import shutil
from time import sleep
from PIL import Image
import os


appleName = 0

while True:
    original = r'..\save-me\apple.jpg'
    target = r'..\save-me\appleTest\apple{}.jpg'.format(appleName)
    print('attempting copy')
    appleName = appleName + 1
