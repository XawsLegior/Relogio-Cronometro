# -*- coding: utf-8 -*- --noconsole

import sys, time
from datetime import datetime
from PySide2 import QtCore, QtGui, QtWidgets
from cybersecp import Ui_Dialog
from PyQt5.QtCore import QThread, pyqtSignal

iniciado = 0
cron = 0
zerar = 0
hr_inicial = "00:00:00"
class relogio(QThread):
    atualiza_relogio = pyqtSignal(str)
    def __init__(self):
        super(relogio, self).__init__()

    def run(self):
        while True:
            rel = datetime.now().strftime('%H:%M:%S')
            self.atualiza_relogio.emit(rel)
            time.sleep(1)

class cronometro(QThread):
    atualiza_cronometro = pyqtSignal(str)
    def __init__(self):
        super(cronometro, self).__init__()

    def run(self):
        global iniciado, cron, hr_inicial
        minuto = 0
        hora = 0
        while True:
            if iniciado == 1:
                hr_quebra = hr_inicial.split(":")
                cron+=1
                hr_quebra[0] = int(hr_quebra[0])
                hr_quebra[1] = int(hr_quebra[1])
                hr_quebra[2] = int(hr_quebra[2])
                
                if hr_quebra[1] < 9: 
                    conc = '0' + str(hr_quebra[1])
                    hr_quebra[1] = str(conc)
                if hr_quebra[0] < 9:
                    conc = '0' + str(hr_quebra[0])
                    hr_quebra[0] = str(conc)

                if hr_quebra[2] < 59: #SEGUNDOS
                    if hr_quebra[2] < 9:
                        hr_quebra[2] = str(hr_quebra[2])
                        hr_quebra[2] = str('0') + str(cron)
                    else:
                        hr_quebra[2] = cron

                elif int(hr_quebra[1]) < 59: #MINUTO
                    hr_quebra[2] = str('00')
                    cron = 0
                    if int(hr_quebra[1]) < 9:
                        minuto+=1
                        hr_quebra[1] = str(hr_quebra[1])
                        hr_quebra[1] = str('0') + str(minuto)
                    else:
                        hr_quebra[1] = minuto
                elif int(hr_quebra[0] > 59):
                    hora = 0
                    minuto = 0
                    cron = 0
                    hr_quebra[2] = str('00')
                    hr_quebra[1] = str('00')
                else: #HORA
                    minuto = 0
                    cron = 0
                    hr_quebra[2] = str('00')
                    hr_quebra[1] = str('00')
                    hora+=1
                    if hr_quebra[0] < 23:
                        if hr_quebra[0] < 9:
                            hr_quebra[0] = str('0') + str(hora)
                        else:
                            hr_quebra[0] = hora
                    else:
                        hr_quebra[0] = "00"
                hr_inicial = str(hr_quebra[0]) + ':' + str(hr_quebra[1]) + ':' + str(hr_quebra[2])
                self.atualiza_cronometro.emit(hr_inicial)
                time.sleep(1)
            else:
                break


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.relogio = relogio()
        self.relogio.start()
        self.relogio.atualiza_relogio.connect(self.atualiza_relogio)

        self.pushButton.clicked.connect(self.iniciar) #INICIAR/PARAR
        self.pushButton_2.clicked.connect(self.zerar) #ZERAR

    def atualiza_relogio(self, rel):
        self.label.setText(rel)

    def atualiza_cronometro(self, cron):
        self.label_3.setText(cron)

    def iniciar(self):
        global iniciado, hr_atual
        if iniciado == 0:
            iniciado = 1
            self.pushButton.setStyleSheet("background: gray; color:white; font-weight:bold")
            self.pushButton.setText("PARAR")
            self.cronometro = cronometro()
            self.cronometro.start()

            self.cronometro.atualiza_cronometro.connect(self.atualiza_cronometro)
        else:
            iniciado = 0
            self.pushButton.setStyleSheet("background: purple; color:white; font-weight:bold")
            self.pushButton.setText("INICIAR")
            self.cronometro = cronometro()

    def zerar(self):
        global iniciado, cron, hr_inicial
        cron = 0
        iniciado = 0
        hr_inicial = "00:00:00"
        self.label_3.setText(hr_inicial)
        self.pushButton.setStyleSheet("background: purple; color:white; font-weight:bold")
        self.pushButton.setText("INICIAR")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())