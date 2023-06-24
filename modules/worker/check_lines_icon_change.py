import os.path

from PyQt5.QtCore import QTimer


def lines_icon_change(self):
    if not self.file_path:
        self.Select_icon_5.setText("ВЫБЕРИТЕ ФАЙЛ")
        QTimer.singleShot(1250, lambda: self.Select_icon_5.setText("Сменить иконку"))
        return 1
    if not os.path.isfile(self.file_path):
        self.Select_icon_5.setText("ФАЙЛ НЕ НАЙДЕН")
        QTimer.singleShot(1250, lambda: self.Select_icon_5.setText("Сменить иконку"))
        return 1
    if not self.icon_path:
        self.Select_icon_5.setText("ВЫБЕРИТЕ ИКОНКУ")
        QTimer.singleShot(1250, lambda: self.Select_icon_5.setText("Сменить иконку"))
        return 1
    if not os.path.isfile(self.icon_path):
        self.Select_icon_5.setText("ИКОНКА НЕ НАЙДЕНА")
        QTimer.singleShot(1250, lambda: self.Select_icon_5.setText("Сменить иконку"))
        return 1
