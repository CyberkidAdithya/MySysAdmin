from PyQt5 import uic
from subprocess import Popen
from PyQt5.QtWidgets import (QMainWindow,
QMessageBox)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # load the UI
        uic.loadUi('login.ui', self)
        # assign functions to buttons
        # self.lineEdit_2.setEchoMode(self, QLineEdit.Password)
        self.pushButton_1.clicked.connect(self.clicked_submit)
        self.pushButton_2.clicked.connect(self.clicked_forgot)
        # show UI
        self.show()
    def clicked_submit(self):
        name = self.lineEdit_1.text()
        password = self.lineEdit_2.text()
        if len(name) < 1 or len(password) < 1:
            QMessageBox.about(self, "Warning",
            "Please enter a name !")
        # CHANGE CREDENTIALS HERE
        elif name == "astraea" and password == "9876":
            QMessageBox.about(self, "Greeting",
            "Welcome Back {}".format(name.capitalize()))
            Popen(['python', 'clock.py'])
            self.close()
        else:
            QMessageBox.about(self, "Warning",
            "Login failed! Try again.")
    def clicked_forgot(self):
        print("FORGOT PASSWORD")
        pass