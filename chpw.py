# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chpw.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(459, 363)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 90, 171, 22))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 90, 171, 22))
        self.commandLinkButton = QCommandLinkButton(Form)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(110, 260, 185, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Altes Passwort", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Neues Passwort", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Form", u"\u00dcbernehmen", None))
    # retranslateUi

