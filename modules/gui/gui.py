from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon

# Иконка
from modules.gui import icon_rc

# Выбор файлов
from modules.fileopen.open_file import file_open
from modules.fileopen.open_icon import icon_open

# Кнопки актив/пассив
from modules.gui.buttons_active import make_buttons_active
from modules.gui.buttons_inactive import make_buttons_inactive

# Окно ошибок и смнена режима окна
from modules.gui.error_window import show_error_message
from modules.gui.window_mode_changer import change_mode_down, change_mode_up

# Проверка на пустоту линий
from modules.worker import check_lines_file_pump
from modules.worker import check_lines_icon_change

# Потоки
from modules.worker.change_icon import ChangeIcon
from modules.worker.pump_file import PumpFile


class Ui_ICP(QtWidgets.QMainWindow):
    def __init__(self, version, pump_mb):
        super().__init__()
        self.file_path = None
        self.icon_path = None
        self.icon_path_select = None
        self.file_path_select = None
        self.version = version
        self.pump_mb = pump_mb
        self.setObjectName(f"Icon Changer & Pumper {self.version}")
        self.setWindowIcon(QIcon(':/icon/icon.ico'))
        self.window_mode = 0
        self.resize(435, 340)
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowCloseButtonHint
            | Qt.WindowMinimizeButtonHint
            | Qt.WindowMaximizeButtonHint
        )
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(435, 340))
        self.setMaximumSize(QtCore.QSize(435, 340))
        self.centralwidget = QtWidgets.QWidget(self)  # replace MainWindow with self here
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(395, 170, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.windows_mode_2 = QtWidgets.QPushButton(self.centralwidget)
        self.windows_mode_2.clicked.connect(self.windows_mode_down)
        self.windows_mode_2.setGeometry(QtCore.QRect(318, 316, 56, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)

        font.setWeight(50)
        self.windows_mode_2.setFont(font)
        self.windows_mode_2.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;\n"
        )
        self.windows_mode_2.setObjectName("windows_mode_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(5, 85, 425, 76))
        self.frame_2.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "border-radius: 10px;"
        )
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(5, 5, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
        )
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.Select_icon = QtWidgets.QPushButton(self.frame_2)
        self.Select_icon.clicked.connect(self.click_select_icon)
        self.Select_icon.setGeometry(QtCore.QRect(325, 40, 96, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setUnderline(True)
        self.Select_icon.setFont(font)
        self.Select_icon.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color:rgb(40, 40, 40);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.Select_icon.setObjectName("Select_icon")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(5, 40, 315, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "background-color: rgb(103, 103, 103);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
            "padding-left: 2px;\n"
            "padding-right: 2px;\n"
        )
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.Select_icon.raise_()
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 551, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setGeometry(QtCore.QRect(5, 256, 426, 56))
        self.frame_5.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "border-radius: 10px;\n"
        )
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.Select_icon_4 = QtWidgets.QPushButton(self.frame_5)
        self.Select_icon_4.clicked.connect(self.click_pump_file)
        self.Select_icon_4.setGeometry(QtCore.QRect(5, 5, 206, 46))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Select_icon_4.setFont(font)
        self.Select_icon_4.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color:rgb(40, 40, 40);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.Select_icon_4.setObjectName("Select_icon_4")
        self.Select_icon_5 = QtWidgets.QPushButton(self.frame_5)
        self.Select_icon_5.clicked.connect(self.click_icon_file)
        self.Select_icon_5.setGeometry(QtCore.QRect(215, 5, 206, 46))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Select_icon_5.setFont(font)
        self.Select_icon_5.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color:rgb(40, 40, 40);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.Select_icon_5.setObjectName("Select_icon_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(6, 316, 70, 20))
        self.frame_7.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "border-radius: 6px;"
        )
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 71, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(351, 316, 60, 20))
        self.frame_8.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "border-radius: 8px;"
        )
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(5, 210, 426, 41))
        self.frame_4.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "border-radius: 10px;\n"
        )
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton.setGeometry(QtCore.QRect(140, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
        )
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(5, 5, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
        )
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setIndent(0)
        self.label_7.setObjectName("label_7")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
        )
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(210, 10, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setToolTip("")
        self.label_8.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;"
        )
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setToolTip(
            "Работает с Meta/Redline\n"
            "Маска ICON"
        )
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(390, 10, 21, 21))
        self.label_9.setToolTip(
            "Должно работать с 64/32 бит .Net билдами,\n"
            "Совместимо с pyinstaller билдами\n"
            "Маска ICON,ICONGROUP"
        )
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;"
        )
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(5, 165, 426, 41))
        self.frame_3.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "border-radius: 10px;\n"
        )
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(5, 5, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
        )
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 0, 245, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setAcceptDrops(False)
        self.horizontalSlider.setStyleSheet(
            "QSlider::groove:horizontal {\n"
            "    border: 1px solid;\n"
            "    border-color: rgb(70, 70, 70);\n"
            "    border-radius: 10px;\n"
            "    height: 20px;\n"
            "    background: rgb(103, 103, 103);\n"
            "    margin: 2px 0;\n"
            "}\n"
            "\n"
            "QSlider::handle:horizontal {\n"
            "    background: rgb(70, 70, 70);\n"
            "    border: 1px solid #000000;\n"
            "    border-radius: 6px;\n"
            "    width: 6px;\n"
            "    margin: -2px 0;\n"
            "    border-radius: 3px;\n"
            "}"
        )
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setPageStep(50)
        self.horizontalSlider.setProperty("value", self.pump_mb)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 165, 30, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
        )
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.windows_mode_1 = QtWidgets.QPushButton(self.centralwidget)
        self.windows_mode_1.clicked.connect(self.windows_mode_up)
        self.windows_mode_1.setGeometry(QtCore.QRect(374, 316, 56, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.windows_mode_1.setFont(font)
        self.windows_mode_1.setStyleSheet(
            "background-color: rgb(70, 70, 70);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 8px;"
        )
        self.windows_mode_1.setObjectName("windows_mode_1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(5, 5, 425, 76))
        self.frame.setStyleSheet(
            "background-color: rgb(52, 52, 52);\n"
            "border-radius: 10px;"
        )
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(5, 40, 315, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
            "background-color: rgb(103, 103, 103);\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
            "padding-left: 2px;\n"
            "padding-right: 2px;\n"
        )
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Select_file = QtWidgets.QPushButton(self.frame)
        self.Select_file.clicked.connect(self.click_select_file)
        self.Select_file.setGeometry(QtCore.QRect(325, 40, 96, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setUnderline(True)
        self.Select_file.setFont(font)
        self.Select_file.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(70, 70, 70);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color:rgb(40, 40, 40);\n"
            "    color: rgb(255, 255, 255);\n"
            "    border-radius: 10px;\n"
            "}"
        )
        self.Select_file.setObjectName("Select_file")
        self.frame_6.raise_()
        self.frame_8.raise_()
        self.windows_mode_2.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.windows_mode_1.raise_()
        self.frame_4.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", f"Icon Changer & Pumper {self.version}"))
        self.label_5.setText(_translate("MainWindow", "1000"))
        self.windows_mode_2.setText(_translate("MainWindow", "Обычно"))
        self.label_4.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:12pt;\">Иконка: </span></p></body></html>"
            )
        )
        self.Select_icon.setText(_translate("MainWindow", "Выбрать..."))
        self.Select_icon_4.setText(_translate("MainWindow", "Пампить"))
        self.Select_icon_5.setText(_translate("MainWindow", "Сменить иконку"))
        self.label_6.setText(
            _translate(
                "ICP",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; color:#bfbfbf;\"><a href=\"https://zelenka.guru/members/6114672/\">By rx580</a></span></p></body></html>"
            )
        )
        self.radioButton.setText(_translate("MainWindow", "Native"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Стаб:</p></body></html>"))
        self.radioButton_2.setText(_translate("MainWindow", ".Net 32/64"))
        self.label_8.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">?</span></p></body></html>"
            )
        )
        self.label_9.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">?</span></p></body></html>"
            )
        )
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Памп (мб):</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><span style=\" font-size:12pt;\">EXE файл: </span></p></body></html>"
            )
        )
        self.windows_mode_1.setText(_translate("MainWindow", "Сверху"))
        self.Select_file.setText(_translate("MainWindow", "Выбрать..."))

    def windows_mode_up(self):
        change_mode_up(self)

    def windows_mode_down(self):
        change_mode_down(self)

    def click_select_file(self):
        file_open(self)

    def click_select_icon(self):
        icon_open(self)

    def click_icon_file(self):
        self.icon_path = self.lineEdit.text()
        self.file_path = self.lineEdit_2.text()

        if check_lines_icon_change.lines_icon_change(self) == 1:
            return

        if self.radioButton.isChecked():
            build_type = "native"
        elif self.radioButton_2.isChecked():
            build_type = "net"

        make_buttons_inactive(self)
        self.icon_changer = ChangeIcon(self.file_path, self.icon_path, build_type)
        self.icon_changer.icon_succeful.connect(self.succeful_icon_change)
        self.icon_changer.icon_error.connect(self.error_icon_change)
        self.icon_changer.start()

    def succeful_icon_change(self):
        self.Select_icon_5.setText("УСПЕШНО")
        QTimer.singleShot(1250, lambda: self.Select_icon_5.setText("Сменить иконку"))
        make_buttons_active(self)

    def error_icon_change(self, error):
        self.Select_icon_5.setText("ОШИБКА")
        show_error_message(error)
        QTimer.singleShot(1250, lambda: self.Select_icon_5.setText("Сменить иконку"))
        make_buttons_active(self)

    def click_pump_file(self):
        self.file_path = self.lineEdit_2.text()
        self.pump_size = self.horizontalSlider.value()

        if check_lines_file_pump.check_pump_lines(self) == 1:
            return
        make_buttons_inactive(self)
        self.file_pumper = PumpFile(self.file_path, self.pump_size)
        self.file_pumper.pump_succeful.connect(self.succeful_file_pump)
        self.file_pumper.pump_error.connect(self.error_file_pump)
        self.file_pumper.start()

    def succeful_file_pump(self):
        self.Select_icon_4.setText("УСПЕШНО")
        QTimer.singleShot(1250, lambda: self.Select_icon_4.setText("Сменить иконку"))
        make_buttons_active(self)

    def error_file_pump(self, error):
        self.Select_icon_4.setText("ОШИБКА")
        show_error_message(error)
        QTimer.singleShot(1250, lambda: self.Select_icon_5.setText("Сменить иконку"))
        make_buttons_active(self)
