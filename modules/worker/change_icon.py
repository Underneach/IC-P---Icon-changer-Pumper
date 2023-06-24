import subprocess

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal


class ChangeIcon(QThread):
    icon_succeful = pyqtSignal()
    icon_error = pyqtSignal(str)

    def __init__(self, file_path, icon_path, build_type):
        super().__init__()
        self.file_path = file_path
        self.icon_path = icon_path
        self.build_type = build_type

    def run(self):

        ph_name = "ResourceHacker.exe"

        if self.build_type == "native":
            try:
                args = [
                    '-open', self.file_path,  # Обрамляем self.file_path кавычками
                    '-action', 'delete',
                    '-mask', 'ICON,,',  # Удаляем иконку
                    '-save', self.file_path,  # Обрамляем self.file_path кавычками
                ]
                subprocess.Popen([ph_name] + args, shell=True)

                args_2 = [
                    '-open', self.file_path,  # Обрамляем self.file_path кавычками
                    '-res', self.icon_path,  # Обрамляем self.icon_path кавычками
                    '-action', 'addoverwrite',
                    '-mask', 'ICON,1,',  # Добавляем иконку
                    '-save', self.file_path,  # Обрамляем self.file_path кавычками
                ]

                subprocess.Popen([ph_name] + args_2, shell=True)
                self.icon_succeful.emit()

            except Exception as error:
                self.icon_error.emit(str(error))

        elif self.build_type == "net":
            try:
                args = [
                    '-open', self.file_path,
                    '-action', 'delete',
                    '-mask', 'ICON,ICONGROUP,',
                    '-save', self.file_path,
                ]

                subprocess.run([ph_name] + args, shell=True)

                args_2 = [
                    '-open', self.file_path,
                    '-resource', self.icon_path,
                    '-mask', 'ICON,1,',
                    '-action', 'addoverwrite',
                    '-save', self.file_path,
                ]

                subprocess.run([ph_name] + args_2, shell=True)
                self.icon_succeful.emit()

            except Exception as error:
                self.icon_error.emit(str(error))
