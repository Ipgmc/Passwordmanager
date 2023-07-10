# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pw_incorrect.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)

class Ui_Warnung(object):
    def setupUi(self, Warnung):
        if not Warnung.objectName():
            Warnung.setObjectName(u"Warnung")
        Warnung.resize(400, 300)
        Warnung.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.buttonBox = QDialogButtonBox(Warnung)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 250, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Warnung)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 221))
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Warnung)

        QMetaObject.connectSlotsByName(Warnung)
    # setupUi

    def retranslateUi(self, Warnung):
        Warnung.setWindowTitle(QCoreApplication.translate("Warnung", u"Warnung", None))
        self.label.setText(QCoreApplication.translate("Warnung", u"Passwort falsch", None))
    # retranslateUi

