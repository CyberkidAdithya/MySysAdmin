# from PyQt5.QtGui import * # from PyQt5.uic import loadUiType
# from PyQt5.QtWidgets import QApplication # from PyQt5 import QtWidgets, QtCore, QtGui, uic
# import pyttsx3

import os, sys, time
from PyQt5 import uic #to load the UI file (made with designer)
from PyQt5.QtCore import QByteArray #to make array of frames
from PyQt5.QtGui import QMovie #to play gif files
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton)

#initialize voice voiceAI
# voiceAI = pyttsx3.init() #sapy5 - windows

#----------Your classes starts here----------

# class newVoice:
#     def __init__(self):
#     #DEFINE VOICE PROPERTIES
#         rate = voiceAI.getProperty('rate') 
#         volume = voiceAI.getProperty('volume')
#         voice = voiceAI.getProperty('voices')
#     #INTIALIZE VOICE PROPERTIES
#         voiceAI.setProperty('rate', 180)
#         voiceAI.setProperty('volume',1.0)
#     #UPDATE VOICE PROPERTIES
#         # voiceAI.setProperty('voice', voices[0].id) #male
#         # voiceAI.setProperty('voice', voices[1].id) #female
#         voiceAI.setProperty('voice','default')
#     def speak(self, audio):
#     #TEXT TO SPEECH
#         voiceAI.say(audio)
#         voiceAI.runAndWait()
#VOICE OBJECT
# nirvana = newVoice()

#----------Your functions starts here----------  

def closeUI():
    print("Shutting Down")
    print("closing UI")
    newlabel1.stop()
    time.sleep(3)
    exit()

def authenticate():
    print("Face Recognition activated")
    print("Activated FR, Show face to webcam !")
    import FRwebcam
def startSQL():
    print("starting SQL service !")
    print("mySQL/Mariadb started !")
def update():
    try:
        os.system("sudo -S apt-get update")
        print("Updated !")
        print("Updated !")
    except Exception as e:
        print("Error: ",e)
def upgrade():
    try:
        os.system("sudo -S apt-get upgrade -y")
        print("Upgraded !")
        print("Upgraded !")
    except Exception as e:
        print("Error: ",e)

#----------Your program code starts here----------
# window.setFixedSize(1920,1080)

#get the form and window class
# print("Powering On")
print("loading UI")
Form, Window = uic.loadUiType("desktop.ui")

#MAKE APP
app = QApplication(sys.argv)

#LOAD WINDOW
window = Window() #create a new UI object
form = Form() #create a new form object
form.setupUi(window) #load UI to form output
window.show() #display output in form output

#PLAY GIFs
newlabel1 = QLabel()
newlabel1 = QMovie("./resources/circle.gif", QByteArray())
newlabel1.setCacheMode(QMovie.CacheAll)
form.jarvisGIF.setMovie(newlabel1)
newlabel1.start()

#CLOSE WINDOW
form.Btnexit.clicked.connect(closeUI)
form.Btn1.clicked.connect(authenticate)
form.Btn2.clicked.connect(startSQL)
form.Btn3.clicked.connect(update)
form.Btn4.clicked.connect(upgrade)

#----------Your code ends here----------

#RUN APP
# sys.exit(app.exec())
app.exec()

#------------------------
# window2 = Window()
# form2 = Form()
# form2.setupUi(window2)
# window2.show()