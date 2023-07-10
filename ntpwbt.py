# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entpw_Bt1.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(421, 157)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 60, 171, 22))
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setInputMask(u"")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.bst = QPushButton(Form)
        self.bst.setObjectName(u"bst")
        self.bst.setGeometry(QRect(130, 100, 141, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Passwort", None))
        self.bst.setText(QCoreApplication.translate("Form", u"Best\u00e4tigen", None))
    # retranslateUi

