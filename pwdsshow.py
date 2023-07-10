# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pwdsshow.ui'
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
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QSizePolicy, QWidget)

class Ui_wind(object):
    def setupUi(self, wind):
        if not wind.objectName():
            wind.setObjectName(u"wind")
        wind.resize(400, 300)
        self.pte = QPlainTextEdit(wind)
        self.pte.setObjectName(u"pte")
        self.pte.setGeometry(QRect(10, 10, 311, 271))
        font = QFont()
        font.setPointSize(12)
        self.pte.setFont(font)
        self.pte.setReadOnly(True)
        self.pte.setTextInteractionFlags(Qt.NoTextInteraction)

        self.retranslateUi(wind)

        QMetaObject.connectSlotsByName(wind)
    # setupUi

    def retranslateUi(self, wind):
        wind.setWindowTitle(QCoreApplication.translate("wind", u"Passw\u00f6rterl", None))
        self.pte.setPlainText("")
    # retranslateUi

