# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cybersecp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,QRect, QSize, Qt)
from PySide2.QtGui import (QIcon)
from PySide2.QtWidgets import *
import visual.resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowIcon(QIcon(":/icons/icon.ico"))
        Dialog.resize(421, 340)
        Dialog.setMinimumSize(QSize(100, 100))
        Dialog.setMaximumSize(QSize(562, 387))
        Dialog.setStyleSheet(u"background: qlineargradient( x1:0 y1:0, x2:1 y2:1, stop:0 SeaGreen, stop:1 LimeGreen);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 50, 151, 51))
        self.label.setStyleSheet(u"background: 0;\n"
"border-image:0;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 30px;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 130, 191, 61))
        self.label_2.setStyleSheet(u"margin-left:10px;background:transparent;border-image:0;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 20px")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 140, 401, 181))
        self.widget.setContextMenuPolicy(Qt.PreventContextMenu)
        self.widget.setStyleSheet(u"background: rgb(255,0,0, 0.8);\n"
"border-image:0;\n"
"border:2px solid black;\n"
"border-radius: 10px")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 40, 131, 41))
        self.label_3.setStyleSheet(u"background: 0;\n"
"font-size: 25px;\n"
"color: white;\n"
"font-weight: bold;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 110, 81, 31))
        self.pushButton.setStyleSheet(u"background: purple;\n"
"color:white;\n"
"font-weight: bold;")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 110, 75, 31))
        self.pushButton_2.setStyleSheet(u"background: purple;\n"
"color:white;\n"
"font-weight: bold;")
        self.widget.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Welson Cron", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"12:00:03", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"CRONOMETRO", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"INICIAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"ZERAR", None))
    # retranslateUi

