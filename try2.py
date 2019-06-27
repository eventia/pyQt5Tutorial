import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import win32api, win32con


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.x_le = QLineEdit()
        self.y_le = QLineEdit()
        self.t_le = QLineEdit()
        self.start_btn = QPushButton('Start', self)
        self.timer = QTimer()

        self.initUI()

    def initUI(self):

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel('x 위치: '))
        hbox1.addWidget(self.x_le)
        hbox1.addWidget(QLabel('y 위치: '))
        hbox1.addWidget(self.y_le)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(QLabel('Delay: '))
        hbox2.addWidget(self.t_le)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.start_btn)
        hbox3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

        self.start_btn.clicked.connect(self.start_btn_click)

        self.setWindowTitle('Repeated Click')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def start_btn_click(self):

        delay = int(self.t_le.text())
        self.timer.start(delay*1000)
        self.timer.timeout.connect(self.mouse_click)

    def mouse_click(self):

        x = int(self.x_le.text())
        y = int(self.y_le.text())

        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
