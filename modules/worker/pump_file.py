from PyQt5.QtCore import QThread, pyqtSignal


class PumpFile(QThread):
    pump_succeful = pyqtSignal()
    pump_error = pyqtSignal(str)

    def __init__(self, file_path, pump_size):
        super().__init__()
        self.file_path = file_path
        self.pump_size = pump_size

    def run(self):
        try:
            b_fSize = self.pump_size * pow(1024, 2)
            buffer = 256
            pumpFile = open(self.file_path, "wb")
            for i in range(int(b_fSize / buffer)):
                pumpFile.write((b"0" * buffer))
            pumpFile.close()
            self.pump_succeful.emit()

        except Exception as error:
            self.pump_error.emit(str(error))
