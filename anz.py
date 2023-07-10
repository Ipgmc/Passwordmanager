# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
 
# class for scrollable label
class ScrollLabel(QScrollArea):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QVBoxLayout(content)
 
        # creating label
        self.label = QLabel(content)
 
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)
 
    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Passwörter ")
 
        # setting geometry
        self.setGeometry(100, 100, 700, 920)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
    # method for widgets
    def UiComponents(self):
        tx=open("Passwords.txt", "r")
        # text to show in label
        text = tx.read()
        
        
        # creating scroll label
        label = ScrollLabel(self)
 
        # setting text to the label
        label.setText(text)
        #label.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
#"color: rgb(255, 255, 255);")
        #label.setFont(QFont("Arial", 12))
        label.setFont(QFont('Arial', 15))
        # setting geometry
        label.setGeometry(200, 100, 400, 800)
        
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
window.show()
 
# start the app
sys.exit(App.exec())