def make_buttons_inactive(self):
    self.Select_icon_5.setEnabled(False)
    self.Select_icon_5.setStyleSheet(
        "QPushButton {\n"
        "    background-color: rgb(50, 50, 50);\n"
        "    color: rgb(205, 205, 205);\n"
        "    border-radius: 10px;\n"
        "}\n"
    )

    self.Select_icon_4.setEnabled(False)
    self.Select_icon_4.setStyleSheet(
        "QPushButton {\n"
        "    background-color: rgb(50, 50, 50);\n"
        "    color: rgb(205, 205, 205);\n"
        "    border-radius: 10px;\n"
        "}\n"
    )
