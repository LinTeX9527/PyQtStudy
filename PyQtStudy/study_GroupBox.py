#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-18 10:11:54

@author: lintex9527@yeah.net
"""

"""
GroupBox 本身是一个有标签的边框，只能装载一个容器，例如布局管理器，用来明确的指示布局分组。

构造方法
=======
groupbox = QGroupBox(title)

常用方法
=======
groupbox.setTitle(title)

groupbox.setLayout(childLayout)
这是GropBox最常用的方式，为其添加一个子布局管理器

groupbox.setAlignment(alignment)
设定子空间的对齐方式，默认是左对齐，可以使用下面的值：
Qt.AlignLeft
Qt.AlignRight
Qt.AlignHCenter

groupbox.setCheckable(checkable)
设定所有的子元素（CheckBox, RadioButton）是否可以选中

groupbox.isChecked()
检查GroupBox 是否被选中

groupbox.setChecked(True)
设置GroupBox被选中，其中的复选框会添加一个标记；如果设置为False，那么复选框会移除这个标记

"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox
from PyQt5.QtWidgets import QVBoxLayout, QRadioButton
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 QGroupBox")

        layout = QGridLayout()
        self.setLayout(layout)

        groupbox = QGroupBox("GroupBox 示例")
        groupbox.setCheckable(True)
        layout.addWidget(groupbox)

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        radiobutton = QRadioButton("复选框1")
        radiobutton.setChecked(True)
        vbox.addWidget(radiobutton)

        radiobutton = QRadioButton("RadioButton 2")
        vbox.addWidget(radiobutton)

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
