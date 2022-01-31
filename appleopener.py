from PIL import Image

appleName = 0

while True:
    im = Image.open(r'..\save-me\appleTest\apple{}.jpg'.format(appleName))
    im.show()
    appleName = appleName + 1
