import keyboard
import webbrowser

counter = 0

while True:
    #T macro that makes you open ten tabs when you press T
    keyboard.wait('T')
    print("Did you mean 'Troll'?")
    while counter < 10:
        webbrowser.open('https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/220px-Trollface_non-free.png')
        counter = counter + 1
    if counter >= 10:
        counter = 0
