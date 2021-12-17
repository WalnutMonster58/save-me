import tkinter
import webbrowser
from time import sleep
#add functions here

def why():
    seconds = 5

    webbrowser.open('https://www.google.com/')
    sleep(seconds)
    while True:
        webbrowser.open('https://static.wikia.nocookie.net/jerma-lore/images/e/e3/JermaSus.jpg/revision/latest?cb=20201206225609')
        

def schoology():
    webbrowser.open('https://schoology.ytech.edu/login/ldap?&school=281446774')

window = tkinter.Tk()
#add things here
b1 = tkinter.Button(text='amogus', command=why, width=50)
b1.pack()

b2 = tkinter.Button(text='text', command=schoology, width=50)
b2.pack()


window.mainloop()
