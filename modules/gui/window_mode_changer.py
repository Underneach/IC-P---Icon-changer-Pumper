from PyQt5.QtCore import Qt


def change_mode_down(self):
    if self.window_mode == 1:
        self.windows_mode_2.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;\n"
        )
        self.windows_mode_1.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;\n"
        )
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowCloseButtonHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )
        self.show()
        self.window_mode = 0
    else:
        return


def change_mode_up(self):
    if self.window_mode == 0:
        self.windows_mode_1.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: outset;\n"
            "border-radius: 8px;\n"
        )
        self.windows_mode_2.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: outset;\n"
            "border-radius: 8px;\n"
        )
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowStaysOnTopHint
        )
        self.show()
        self.window_mode = 1
    else:
        return
