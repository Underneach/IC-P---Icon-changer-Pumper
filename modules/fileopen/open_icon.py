from PyQt5.QtWidgets import QFileDialog
from modules.gui.error_window import show_error_message


def icon_open(self):
    try:
        self.icon_path_select, _ = QFileDialog.getOpenFileName(None, 'Open File', './', 'ICON File (*.ico)')
        self.lineEdit.setText(self.icon_path_select)
        self.lineEdit.end(False)
    except Exception as e:
        show_error_message(str(e))
