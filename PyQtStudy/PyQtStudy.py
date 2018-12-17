#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PyQt5 学习记录
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("Hello PyQt5")

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)

        btn_opacity_half = QPushButton("半透明")
        layout.addWidget(btn_opacity_half)

    def initGUI(self, title):
        startx = 800
        starty = 400
        width  = 480
        height = 320
        self.setGeometry(startx, starty, width, height)
        self.setWindowTitle(title)
        self.setWindowOpacity(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MyWindow()
    w.show()

    sys.exit(app.exec_())