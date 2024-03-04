# -*- coding: utf-8 -*-
import sys
from WinLogic import WindowLogic
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowLogic()
    win.show()
    sys.exit(app.exec_())
