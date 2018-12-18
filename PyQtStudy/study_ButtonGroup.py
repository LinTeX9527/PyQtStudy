#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-18 08:49:30

@author: lintex9527@yeah.net
"""

"""
ButtonGroup 是不可见的对象，用来给按钮分组。常用的场景是把 RadioButton 分组。

构造方法
=======
buttongroup = QButtonGroup()

常用方法
=======
buttongroup.addButton(button, id)
把@button添加到按钮@buttongroup分组中，其中的@id参数可以省略，如果不省略，
就需要指定一个正整数，代表按钮@button在分组中的序号。

buttongroup.removeButton(button)
从分组中移除一个按钮。

buttongroup.buttons()
列出分组中所有的按钮。

buttongroup.button(id)
返回指定序号的按钮。

buttongroup.id(button)
返回指定按钮的序号。

buttongroup.setId(button, id)
按钮加入分组之后，重新设置按钮的序号。

buttongroup.setExclusive(exclusive)
强制设定分组中一次只能选中一个按钮

buttongroup.checkedButton()
如果分组中有按钮是可以处于 checked state，那么通过这个方法找到处于 checked state 状态的这个按钮。

可用的 signals
==============
buttonClicked(button)
buttonClicked(id)

buttonPressed(button)
buttonPressed(id)

buttonReleased(button)
buttonReleased(id)

buttonToggled(button)
buttonToggled(id)
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QButtonGroup
from PyQt5.QtWidgets import QPushButton, QRadioButton, QCheckBox
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 ButtonGroup")

        # 设定窗口的布局管理器为 QGridLayout
        layout = QGridLayout()
        self.setLayout(layout)

        self.buttonGroup = QButtonGroup()
        # # 按钮不是互斥的，即可以同时选中多个按钮
        # self.buttonGroup.setExclusive(False)
        # 按钮是互斥的，即同一时刻只能选中1个按钮
        self.buttonGroup.setExclusive(True)
        # NOTE: 绑定信号与槽函数，信号是 buttonGroup.buttonClicked(id)，槽函数是 on_button_clicked(id)
        self.buttonGroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton("PushButton 1")
        self.buttonGroup.addButton(button, 1)
        layout.addWidget(button, 0, 0)

        button = QPushButton("PushButton 2")
        self.buttonGroup.addButton(button, 2)
        layout.addWidget(button, 0, 1)

        rdBtn = QRadioButton("单选按钮1")
        self.buttonGroup.addButton(rdBtn, 3)
        layout.addWidget(rdBtn, 1, 0)

        rdBtn = QRadioButton("单选按钮2")
        self.buttonGroup.addButton(rdBtn, 4)
        layout.addWidget(rdBtn, 1, 1)

        # 添加了复选框到同一个分组，四个按钮同时只能选择一个。
        checkbox = QCheckBox("复选框1")
        self.buttonGroup.addButton(checkbox, 5)
        layout.addWidget(checkbox, 2, 0)

        checkbox = QCheckBox("复选框2")
        self.buttonGroup.addButton(checkbox, 6)
        layout.addWidget(checkbox, 2, 1)

    def on_button_clicked(self, id):
        """
        遍历按钮组，找到这个按钮
        """
        for button in self.buttonGroup.buttons():
            if button is self.buttonGroup.button(id):
                print("%s was clicked" % (button.text()))

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
