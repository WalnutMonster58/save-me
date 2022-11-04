import keyboard
import webbrowser

#macro for letter L

while True:
    keyboard.wait('l')
    keyboard.press_and_release('backspace')
    keyboard.press('shift')
    keyboard.write('I love men I love men I love men I love men I love men I love men')
    keyboard.release('shift')
    keyboard.press_and_release('enter')
