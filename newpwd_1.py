# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newpwd_1.ui'
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
        Form.resize(543, 219)
        self.entry_login = QLineEdit(Form)
        self.entry_login.setObjectName(u"entry_login")
        self.entry_login.setGeometry(QRect(50, 20, 141, 22))
        self.entry_login.setCursor(QCursor(Qt.ArrowCursor))
        self.entry_pw = QLineEdit(Form)
        self.entry_pw.setObjectName(u"entry_pw")
        self.entry_pw.setGeometry(QRect(50, 80, 141, 22))
        self.entry_using = QLineEdit(Form)
        self.entry_using.setObjectName(u"entry_using")
        self.entry_using.setGeometry(QRect(50, 140, 141, 22))
        self.bt_ok = QPushButton(Form)
        self.bt_ok.setObjectName(u"bt_ok")
        self.bt_ok.setGeometry(QRect(280, 40, 171, 41))
        self.bt_abort = QPushButton(Form)
        self.bt_abort.setObjectName(u"bt_abort")
        self.bt_abort.setGeometry(QRect(280, 100, 171, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Passwort hinzuf\u00fcgen", None))
#if QT_CONFIG(accessibility)
        self.entry_login.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.entry_login.setInputMask("")
        self.entry_login.setPlaceholderText(QCoreApplication.translate("Form", u"Login", None))
        self.entry_pw.setPlaceholderText(QCoreApplication.translate("Form", u"Passwort", None))
        self.entry_using.setPlaceholderText(QCoreApplication.translate("Form", u"Verwendung", None))
        self.bt_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.bt_abort.setText(QCoreApplication.translate("Form", u"Abbrechen", None))
    # retranslateUi

