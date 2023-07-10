import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 180))    
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com") 
        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(200, 32)
        

        self.line2 = QLineEdit(self)
        self.line2.move(80, 60)
        self.line2.resize(200, 32)
       

        self.line3 = QLineEdit(self)
        self.line3.move(80, 100)
        self.line3.resize(200, 32)
        
        

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 140)        

    def clickMethod(self):
        open("p.txt", "a").write('Your name: ' + self.line.text())

        print('Your name: ' + self.line.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() ) 