from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton


def show_error_message(message):
    app = QApplication([])
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Critical)
    error_box.setWindowTitle("Ошибка")
    error_box.setText("Произошла ошибка:")
    error_box.setInformativeText(message)

    ok_button = QPushButton("Ок")
    error_box.addButton(ok_button, QMessageBox.AcceptRole)

    def on_ok_button_clicked():
        error_box.close()

    ok_button.clicked.connect(on_ok_button_clicked)

    error_box.exec_()
