#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on

@author: lintex9527@yeah.net
"""

"""
PyQt5 工程模板
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习")

    def initGUI(self, title):
        """
        设置窗口大小和位置，以及标题
        """
        startx = 800
        starty = 400
        width = 480
        height = 320
        self.setGeometry(startx, starty, width, height)
        self.setWindowTitle(title)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen = MyWindow()
    screen.show()

    sys.exit(app.exec_())

