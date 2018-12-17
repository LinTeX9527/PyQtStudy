#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:34:11 2018

@author: shenglin.zhan@lightningsemi.com
"""

from PyQt5.QtWidgets import *
import sys

"""
参见教程《pyqt5tutorial.pdf》
"""

class Window(QWidget):
    """
    初始化，UI初始化
    """
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PyQt5")

        # 设置最大最小化
        # self.showMinimized()
        # self.showMaximized()
        # self.showFullScreen()

        # 设置最大最小宽度/高度
        # self.setMinimumWidth(320)
        # self.setMaximumWidth(320)
        # self.setMinimumHeight(400)
        # self.setMaximumHeight(400)

        self.setFixedWidth(480)
        self.setFixedHeight(320)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Hello PyQt5")
        layout.addWidget(label, 0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen = Window()
    screen.show()

    sys.exit(app.exec_())

