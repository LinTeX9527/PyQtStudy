#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-17 16:07:02

@author: lintex9527@yeah.net
"""

"""
GridLayout 网格布局，可以动态调整子部件

构造方法
=======
gridlayout = QGridLayout()

常用方法
=======
gridlayout.addWidget(widget)
gridlayout.addWidget(widget, row, column)
gridlayout.addWidget(widget, row, column, rowspan, columnspan, alignment)

@row, @column 从左上角(0, 0)开始的坐标系统
@rowspan, @cloumnspan 指定跨列的数目
@alignment 指定对其方式，可以是以下值：

Qt.AlignmentLeft
Qt.AlignmentRight
Qt.AlignmentHCenter
Qt.AlignmentJustify

也可以嵌套地加入其它的布局管理器
=============================
gridlayout.addLayout(widget)
gridlayout.addLayout(widget, row, column)
gridlayout.addLayout(widget, row, column, rowspan, columnspan, alignment)

返回指定坐标处的子部件
====================
gridlayout.itemAtPosition(row, column)

默认子部件之间是没有空隙的，需要手动调整
====================================
gridlayout.setSpacing(spacing)
@spacing integer 类型，表示像素点个数

可以单独设置 vertical/horizontal 方向的间隙
=========================================
gridlayout.setHorizontalSpacing(spacing)
gridlayout.setVerticalSpacing(spacing)

返回布局管理器中的行数和列数
=========================
gridlayout.rowCount()
gridlayout.columnCount()
"""

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initGUI("GridLayout")

        # 设置GridLayout为当前窗口的布局管理器
        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("C @(0, 0)")
        # TODO: 添加label的属性，让每一个label边界都很明显的显示出来，容易区分GridLayout的格子
        layout.addWidget(label, 0, 0)

        label = QLabel("C++ @(0, 1)")
        layout.addWidget(label, 0, 1)

        label = QLabel("Java @(1, 0) spanning 2 columns")
        layout.addWidget(label, 1, 0, 1, 2)

        label = QLabel("Python @(0, 2) spaning 2 rows")
        layout.addWidget(label, 0, 2, 2, 1)

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
