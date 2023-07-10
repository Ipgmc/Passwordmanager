# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget, QFrame)


class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(1101, 748)
        root.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.actionBeenden = QAction(root)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.actionDokumentation = QAction(root)
        self.actionDokumentation.setObjectName(u"actionDokumentation")
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 1081, 121))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.00568182 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 40, 371, 61))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 160, 311, 81))
        font = QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 250, 311, 81))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 340, 311, 81))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 430, 311, 81))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 520, 311, 81))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(380, 160, 691, 441))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 690, 1081, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(343, 160, 20, 441))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 351, 21))
        self.label_3.setStyleSheet(u"\n"
"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(27, 163, 200);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(740, 60, 351, 21))
        self.label_4.setStyleSheet(u"\n"
"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(27, 163, 200);")
        root.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(root)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1101, 22))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuHilfe = QMenu(self.menubar)
        self.menuHilfe.setObjectName(u"menuHilfe")
        root.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(root)
        self.statusbar.setObjectName(u"statusbar")
        root.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())
        self.menuDatei.addAction(self.actionBeenden)
        self.menuHilfe.addAction(self.actionDokumentation)

        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Passwortspeicher", None))
        self.actionBeenden.setText(QCoreApplication.translate("root", u"Beenden", None))
        self.actionDokumentation.setText(QCoreApplication.translate("root", u"Dokumentation", None))
        self.label.setText(QCoreApplication.translate("root", u"<html><head/><body><p><img src=\":/DateiPasswortschu\u0308tzen_1.jpg\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("root", u"<html><head/><body><p><span style=\" font-size:36pt; color:#0000ff;\">Passwortspeicher</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("root", u"Passw\u00f6rter anzeigen", None))
        self.pushButton_2.setText(QCoreApplication.translate("root", u"Passwort hinzuf\u00fcgen", None))
        self.pushButton_3.setText(QCoreApplication.translate("root", u"Passwort generieren", None))
        self.pushButton_4.setText(QCoreApplication.translate("root", u"Passwortsicherheit \u00fcberpr\u00fcfen", None))
        self.pushButton_5.setText(QCoreApplication.translate("root", u"Generalschl\u00fcssel \u00e4ndern", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.menuDatei.setTitle(QCoreApplication.translate("root", u"Datei", None))
        self.menuHilfe.setTitle(QCoreApplication.translate("root", u"Hilfe", None))
    # retranslateUi

