# https://mainia.tistory.com/5174

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)

app = QApplication([])
dialog = QInputDialog()
dialog.show()
app.exec_()
