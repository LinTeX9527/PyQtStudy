#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QWindow):
    """
    注意这个类继承自 QWindow
    """
    def __init__(self):
        QWindow.__init__(self)

        # self.setTitle("Window")

        # 设置窗口的宽度、高度
        width = 400
        height = 300
        self.resize(width, height)

        startx = 800
        starty = 400
        # 设置窗口的起始坐标 x0, y0
        self.setPosition(startx, starty)
        # 设置窗口的不透明度：0 -- 完全隐形；0.5 -- 半透明；1 -- 完全不透明
        self.setOpacity(0.5)


app = QApplication(sys.argv)

screen = Window()
screen.show()
sys.exit(app.exec_())
