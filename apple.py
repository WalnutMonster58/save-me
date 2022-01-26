import shutil
from time import



appleName = 0

while True:
    original = r'..\save-me\apple.jpg'
    target = r'..\save-me\appleTest\apple{}.jpg'.format(appleName)
    print('attempting copy')
    shutil.copyfile(original, target)
    appleName = appleName + 1
