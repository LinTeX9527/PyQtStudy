#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-18 15:37:02

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QScrollArea
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys

"""
ScrollArea 提供了一个容器来显示另外一个widget，而且还提供了垂直和水平方向的ScrollBar。

构造方法
=======
scrollarea = QScrollArea()

常用方法
=======
scrollarea.setWidget(widget)
添加要显示的部件到其中

scrollarea.widget()
返回其中显示的部件

scrollarea.setAlignment(alignment)
设置要显示的部件的对齐方式，可以是如下值：
Qt.AlignLeft
Qt.AlignRight
Qt.AlignTop
Qt.AlignBottom
Qt.AlignHCenter
Qt.AlignVCenter

scrollarea.setWidgetResizable(True/False)
设置是否其中的部件是否可以自动放大、缩小。
如果为True，则其中的部件自动缩放填充scrollarea所具有的区域；
如果为False，则使用widget自身的大小，并提供 ScrollBar
"""


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 QScrollArea")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        msg = " 我是如来佛祖玉皇大帝观音菩萨指定去西天取经特派使者花果山水帘洞美猴王齐天大圣孙悟空啊，帅到掉渣 " * 50
        label = QLabel(msg)
        label.setWordWrap(True)
        scroll_area = QScrollArea()
        scroll_area.setWidget(label)
        scroll_area.setBackgroundRole(QPalette.Dark)
        mainLayout.addWidget(scroll_area, 0, 0, 1, 1, Qt.AlignJustify)

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
