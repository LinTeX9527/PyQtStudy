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

NOTE: 注意区分 setCheckable() 和 setChecked() 的不同之处
groupbox.setCheckable(checkable)
设置group box 是否显示一个复选框，如果为 True 则显示复选框

groupbox.isChecked()
检查GroupBox 是否被选中

groupbox.setChecked(True)
设置GroupBox被选中，其中的复选框会添加一个标记，而且所有的子元素都可以被选中；
如果设置为False，所有的子元素都被 disable，而且用户不能访问

"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox
from PyQt5.QtWidgets import QVBoxLayout, QRadioButton, QHBoxLayout, QPushButton
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 QGroupBox")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        self.groupbox_hero = QGroupBox("英雄类型")
        self.groupbox_hero.setCheckable(True)
        mainLayout.addWidget(self.groupbox_hero, 0, 0)

        vbox = QVBoxLayout()
        self.groupbox_hero.setLayout(vbox)

        radiobutton = QRadioButton("法师")
        radiobutton.setChecked(True)
        vbox.addWidget(radiobutton)

        radiobutton = QRadioButton("刺客")
        vbox.addWidget(radiobutton)

        self.btn_hero = QPushButton("禁选英雄")
        self.btn_hero.clicked.connect(self.on_btn_clicked)
        mainLayout.addWidget(self.btn_hero, 1, 0)

        self.btn_place = QPushButton("禁选籍贯")
        self.btn_place.clicked.connect(self.on_btn_clicked)
        mainLayout.addWidget(self.btn_place, 1, 1)

        self.groupbox_place = QGroupBox("籍贯")
        self.groupbox_place.setCheckable(True)
        mainLayout.addWidget(self.groupbox_place, 2, 0)

        hbox = QHBoxLayout()
        self.groupbox_place.setLayout(hbox)

        radiobutton = QRadioButton("仙界")
        radiobutton.setChecked(True)
        hbox.addWidget(radiobutton)

        radiobutton = QRadioButton("魔界")
        hbox.addWidget(radiobutton)

        radiobutton = QRadioButton("人界")
        hbox.addWidget(radiobutton)

    def on_btn_clicked(self):
        button = self.sender()
        if button is self.btn_hero:
            print("注意setCheckable() 和 setChecked() 不同之处")
            if button.text() == "禁选英雄":
                self.groupbox_hero.setChecked(False)
                button.setText("选择英雄")
            elif button.text() == "选择英雄":
                self.groupbox_hero.setChecked(True)
                button.setText("禁选英雄")
        elif button is self.btn_place:
            print("注意setCheckable() 和 setChecked() 不同之处")
            if button.text() == "禁选籍贯":
                self.groupbox_place.setCheckable(False)
                button.setText("选择籍贯")
            elif button.text() == "选择籍贯":
                self.groupbox_place.setCheckable(True)
                button.setText("禁选籍贯")
        else:
            print("寻找按钮失败")

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
