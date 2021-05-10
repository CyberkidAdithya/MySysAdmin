#----------PACKAGES----------

import sys, time
from PyQt5.QtWidgets import QApplication

#----------MY MODULES----------

from login import *
from clock import clock_obj
from main import SplashScreen
from sysinfo import GUI_stats

#----------MY PROGRAM----------

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # load the UI
        uic.loadUi('login.ui', self)
        # assign functions to buttons
        self.pushButton_1.clicked.connect(self.clicked_submit)
        self.pushButton_2.clicked.connect(self.clicked_forgot)
        # show UI
        self.show()
    def clicked_submit(self):
        name = self.lineEdit_1.text()
        password = self.lineEdit_2.text()
        if len(name) < 1 or len(password) < 1:	#testcase
            QMessageBox.about(self, "Warning",
            "Please enter a name !")
        # CHANGE CREDENTIALS HERE
        elif name == "astraea" and password == "9876":	#testcase
            QMessageBox.about(self, "Greeting",
            "Welcome Back {}".format(name.capitalize()))
            Popen(['python', 'clock.py'])
            self.close()
        else:	#testcase
            QMessageBox.about(self, "Warning",
            "Login failed! Try again.")
    def clicked_forgot(self):
        print("FORGOT PASSWORD")
        pass

if __name__ == '__main__':
    # print("THERE")	#debug checkpoint 1
    print("Loading Login App")
    app = QApplication(sys.argv)
    window = MyWindow()
    app.exec_()
    window.destroy()
    QApplication.closeAllWindows()
    print("Astraea has logged in")
    time.sleep(3)
    # print("HERE")	#debug checkpoint 2
    print("Loading Clock...")	# debug checkpoint 3
    x = clock_obj()
    print("Loading GUI stats")
    print(GUI_stats())



