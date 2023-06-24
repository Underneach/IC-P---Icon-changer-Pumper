from PyQt5.QtWidgets import QFileDialog
from modules.gui.error_window import show_error_message


def file_open(self):
    try:
        self.file_path_select, _ = QFileDialog.getOpenFileName(None, 'Open File', './', 'EXE or SCR File (*.exe *.scr)')
        self.lineEdit_2.setText(self.file_path_select)
        self.lineEdit_2.end(False)
    except Exception as e:
        show_error_message(str(e))
