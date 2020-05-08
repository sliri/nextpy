# 6.3.3
################


import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 125)  # setting up new voice rate
engine.say("first time i'm using a package in next.py course")
engine.runAndWait()
