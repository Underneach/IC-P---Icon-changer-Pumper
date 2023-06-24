import os
import os.path

from PyQt5.QtCore import QTimer


def check_pump_lines(self):
    if not self.file_path:
        self.Select_icon_4.setText("ВЫБЕРИТЕ ФАЙЛ")
        QTimer.singleShot(1250, lambda: self.Select_icon_4.setText("Пампить"))
        return 1
    if not os.path.isfile(self.file_path):
        self.Select_icon_4.setText("ФАЙЛ НЕ НАЙДЕН")
        QTimer.singleShot(1250, lambda: self.Select_icon_4.setText("Пампить"))
        return 1
