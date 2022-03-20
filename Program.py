# -*- coding: utf-8 -*- --noconsole

import sys, time
from datetime import datetime
from threading import Thread

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from cybersecp import Ui_Dialog
from PyQt5.QtCore import QThread, pyqtSignal

from Threads import Relogio, Cronometro

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.rodando = 1
        Relogio.relogio(self)           # Thread atualizar relógio
        self.cron = Cronometro.cronometro(self)     # Thread atualizar cronometro

        self.pushButton.clicked.connect(self.cronometro) #INICIAR/PARAR
        self.pushButton_2.clicked.connect(self.zerar)  # ZERAR

    def closeEvent(self, event:PySide2.QtGui.QCloseEvent) -> None:
        self.rodando = 0

    def cronometro(self):
        self.cron.iniciar()

    def zerar(self):
        self.cron.zerar()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())