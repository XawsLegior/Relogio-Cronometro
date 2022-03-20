from threading import Thread
import time

class cronometro:
    def __init__(self, parent):
        super(cronometro, self).__init__()
        self.main = parent
        self.rodar_cron = 0     # 0 = parar / 1 = rodar
        self.hora_cron = "00:00:00"

    def iniciar(self):
        if self.rodar_cron == 0:
            self.rodar_cron = 1
            self.main.pushButton.setStyleSheet("background: gray; color:white; font-weight:bold")
            self.main.pushButton.setText("PARAR")
            Thread(target=self.run).start()
        else:
            self.rodar_cron = 0
            self.main.pushButton.setStyleSheet("background: purple; color:white; font-weight:bold")
            self.main.pushButton.setText("INICIAR")

    def zerar(self):
        self.rodar_cron = 0
        self.hora_cron = "00:00:00"
        self.main.label_3.setText(self.hora_cron)
        self.main.pushButton.setStyleSheet("background: purple; color:white; font-weight:bold")
        self.main.pushButton.setText("INICIAR")

    def run(self):
        while self.rodar_cron == 1 and self.main.rodando == 1:
            hora = self.hora_cron.split(":")
            hora[0] = int(hora[0])
            hora[1] = int(hora[1])
            hora[2] = int(hora[2])
            # SEGUNDOS
            if hora[2] < 60:
                hora[2]+=1
            # MINUTOS
            if hora[1] < 60 and hora[2] >= 60:
                hora[2] = "00"
                hora[1] += 1
            # HORAS
            if hora[1] >= 60:
                hora[2] = "00"
                hora[1] = "00"
                hora[0] += 1

            # CONCATENAR COM 0 SE FOR MENOR QUE 2 CARACTERES
            hora[0] = str(hora[0])
            hora[1] = str(hora[1])
            hora[2] = str(hora[2])
            if len(hora[0]) < 2:
                hora[0] = "0" + hora[0]
            if len(hora[1]) < 2:
                hora[1] = "0" + hora[1]
            if len(hora[2]) < 2:
                hora[2] = "0" + hora[2]

            # SETAR NO LABEL
            self.hora_cron = f"{hora[0]}:{hora[1]}:{hora[2]}"
            self.main.label_3.setText(self.hora_cron)
            time.sleep(1)