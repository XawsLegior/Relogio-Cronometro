import threading
from datetime import datetime
import time

class relogio:
    def __init__(self, parent):
        super(relogio, self).__init__()
        self.main = parent
        threading.Thread(target=self.run).start()

    def run(self):
        while self.main.rodando == 1:
            rel = datetime.now().strftime('%H:%M:%S')
            self.main.label.setText(rel)
            time.sleep(1)
