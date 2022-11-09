import string
import random
import math
import tkinter
import webbrowser
import json

message = 0
dataMessage = []
version = '1.0'


def encode():
    message = str(input())
    
    mixedMessage = ''

    for x in message:
        if x != ' ':
            indexedMessage = ord(x)
            dataMessage.append(indexedMessage)
                        
            x = random.randint(97,122)
            
            mixedMessage += chr(x)
        
        else:
            dataMessage.append(x)
            
            mixedMessage += x
        
        
    with open('cipherData.json', 'w') as file:
        json.dump(dataMessage, file)
    print(mixedMessage)

def decode():
    f = open('cipherData.json')
    
    data = json.load(f)
    
    decodedMessage = ''

    
    for i in data:
        
        if i != ' ':
            decodedMessage += str(chr(i))
            
        else: 
            decodedMessage += i
            
    print(decodedMessage)
            
    
window = tkinter.Tk()
window.title('Beta Version: ' + version)
window.geometry('500x500')

b1 = tkinter.Button(text='Encode Message', command=encode, width=50)
b1.pack()

b2 = tkinter.Button(text='Decode Message', command=decode, width=50)
b2.pack()

window.mainloop()
