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
from PyQt5.QtWidgets import QVBoxLayout, QRadioButton, QHBoxLayout
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 QGroupBox")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        groupbox = QGroupBox("英雄类型")
        groupbox.setCheckable(True)
        mainLayout.addWidget(groupbox, 0, 0)

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        radiobutton = QRadioButton("法师")
        radiobutton.setChecked(True)
        vbox.addWidget(radiobutton)

        radiobutton = QRadioButton("刺客")
        vbox.addWidget(radiobutton)

        groupbox2 = QGroupBox("籍贯")
        groupbox2.setCheckable(True)
        mainLayout.addWidget(groupbox2, 1, 0)

        hbox = QHBoxLayout()
        groupbox2.setLayout(hbox)

        radiobutton = QRadioButton("仙界")
        radiobutton.setChecked(True)
        hbox.addWidget(radiobutton)

        radiobutton = QRadioButton("魔界")
        hbox.addWidget(radiobutton)

        radiobutton = QRadioButton("人界")
        hbox.addWidget(radiobutton)

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
