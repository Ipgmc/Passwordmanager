# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'genpwd_1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 298)
        self.pw_generated = QLabel(Form)
        self.pw_generated.setObjectName(u"pw_generated")
        self.pw_generated.setEnabled(True)
        self.pw_generated.setGeometry(QRect(80, 50, 221, 61))
        self.pw_generated.setAcceptDrops(False)
        self.pw_generated.setAlignment(Qt.AlignCenter)
        self.pw_generated.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.generate = QPushButton(Form)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(90, 150, 191, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Passwort generieren", None))
        self.pw_generated.setText("")
        self.generate.setText(QCoreApplication.translate("Form", u"Generieren", None))
    # retranslateUi

