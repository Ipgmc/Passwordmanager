# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chkpwd_1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(380, 290)
        font = QFont()
        font.setBold(True)
        Form.setFont(font)
        self.entpw = QLineEdit(Form)
        self.entpw.setObjectName(u"entpw")
        self.entpw.setGeometry(QRect(70, 20, 221, 22))
        font1 = QFont()
        font1.setBold(False)
        self.entpw.setFont(font1)
        self.check = QPushButton(Form)
        self.check.setObjectName(u"check")
        self.check.setGeometry(QRect(70, 70, 221, 41))
        self.check.setFont(font1)
        self.security = QLabel(Form)
        self.security.setObjectName(u"security")
        self.security.setGeometry(QRect(20, 170, 111, 51))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.security.setFont(font2)
        self.sec_step = QLabel(Form)
        self.sec_step.setObjectName(u"sec_step")
        self.sec_step.setGeometry(QRect(150, 170, 141, 51))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.sec_step.setFont(font3)
        self.sec_step.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Passwortsicherheit \u00fcberpr\u00fcfen", None))
        self.entpw.setPlaceholderText(QCoreApplication.translate("Form", u"Passwort eingeben", None))
        self.check.setText(QCoreApplication.translate("Form", u"\u00dcberpr\u00fcfen", None))
        self.security.setText(QCoreApplication.translate("Form", u"Sicherheit:", None))
        self.sec_step.setText("")
    # retranslateUi

