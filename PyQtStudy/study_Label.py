#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-17 17:21:26

@author: lintex9527@yeah.net
"""

"""
Label 显示一个单词指示另一个控件的用途，或者一个语句，多行、多段落的文本。

构造方法
=======
label = QLabel(text)

常用方法
=======
label.setText(text)
改变文本内容

label.text()
返回文本内容

label.setAlignment(alignment)
默认的对其方式是：从左往右，垂直居中。
水平对齐方式可以是如下值：
Qt.AlignLeft
Qt.AlignHCenter
Qt.AlignRight
Qt.AlignJustify

垂直对齐方式是：
Qt.AlignTop
Qt.AlignVCenter
Qt.AlignBottom
Qt.AlignBaseline

如果要同时制定水平和垂直对齐方式，可以使用 | 符号。

label.setWordWrap(True)
设置是否自动换行。

label.setMargin(margin)
设定外边界的像素个数，默认值为0.

label.setIndent(indent)
设定缩进，以像素个数为单位，默认值为0.

label.setBuddy(widget)
标签中显示助记符，帮助快速访问另外一个控件。
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("QLabel")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("The Story of Dale")
        layout.addWidget(label, 0, 0)

        label = QLabel("Few people could understand Dale's motivation.")
        label.setWordWrap(True)
        layout.addWidget(label, 0, 1)

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
