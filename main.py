import sys
import random
import sys

from PyQt5 import QtWidgets

from modules.gui.gui import Ui_ICP

version = "1.3"

pump_mb = random.randint(100, 500)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_ICP(version, pump_mb)
    window.show()
    sys.exit(app.exec_())
