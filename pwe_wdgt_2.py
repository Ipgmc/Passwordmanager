# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pwe_wdgt_2.ui'
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

class Ui_pweingabe_wdgt_2(object):
    def setupUi(self, pweingabe_wdgt_2):
        if not pweingabe_wdgt_2.objectName():
            pweingabe_wdgt_2.setObjectName(u"pweingabe_wdgt_2")
        pweingabe_wdgt_2.resize(407, 175)
        self.bt_ok_2 = QPushButton(pweingabe_wdgt_2)
        self.bt_ok_2.setObjectName(u"bt_ok_2")
        self.bt_ok_2.setGeometry(QRect(120, 90, 141, 41))
        self.entry_pw_2 = QLineEdit(pweingabe_wdgt_2)
        self.entry_pw_2.setObjectName(u"entry_pw_2")
        self.entry_pw_2.setGeometry(QRect(100, 40, 181, 22))

        self.retranslateUi(pweingabe_wdgt_2)

        QMetaObject.connectSlotsByName(pweingabe_wdgt_2)
    # setupUi

    def retranslateUi(self, pweingabe_wdgt_2):
        pweingabe_wdgt_2.setWindowTitle(QCoreApplication.translate("pweingabe_wdgt_2", u"Bitte Passwort eingeben", None))
        self.bt_ok_2.setText(QCoreApplication.translate("pweingabe_wdgt_2", u"OK", None))
        self.entry_pw_2.setPlaceholderText(QCoreApplication.translate("pweingabe_wdgt_2", u"Passwort", None))
    # retranslateUi

