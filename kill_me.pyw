import tkinter
import webbrowser
from time import sleep
import random
#add functions here

counter = 0




def why():
    seconds = 10

    webbrowser.open('https://www.youtube.com/watch?v=grd-K33tOSM')
    sleep(seconds)
    while True:
        webbrowser.open('https://static.wikia.nocookie.net/jerma-lore/images/e/e3/JermaSus.jpg/revision/latest?cb=20201206225609')


def schoology():
    webbrowser.open('https://schoology.ytech.edu/login/ldap?&school=281446774')

def walnut():
    webbrowser.open('https://www.youtube.com/channel/UC1rHmb-Euu1R0HsVFah3VtQ')

def clickme():
    webbrowser.open('https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/220px-Trollface_non-free.png')

def secondary():
    webbrowser.open('secondary.py')

secondary()

def third():
    webbrowser.open('third.py')

third()
def binary():
    webbrowser.open('littleGuy.py')

binary()

def trollface():
    webbrowser.open('trollface.py')

trollface()

def counter():
    webbrowser.open('counter.py')

counter()

window = tkinter.Tk()
#add things here
b1 = tkinter.Button(text='amogus', command=why, width=50)
b1.pack()

b2 = tkinter.Button(text='text', command=schoology, width=50)
b2.pack()

b3 = tkinter.Button(text='walnut', command=walnut, width=50)
b3.pack()

b4 = tkinter.Button(text='Click Me', command=clickme, width=50)
b4.pack()


window.mainloop()
