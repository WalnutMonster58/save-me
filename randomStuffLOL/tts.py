import pyttsx3


engine = pyttsx3.init()



msg = input("Message: ")

engine.say(msg)




engine.runAndWait()