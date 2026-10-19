from PIL import Image

appleName = 0

while True:
    print('opening apple' + str(appleName))
    im = Image.open(r'..\save-me\appleTest\apple{}.jpg'.format(appleName))
    im.show()
    appleName = appleName + 1
