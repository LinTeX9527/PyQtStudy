#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-17 19:00:54

@author: lintex9527@yeah.net
"""

"""
CheckBox 只有选中或者未选中的状态，每一个都是独立的。

构造方法
=======
checkbox = QCheckBox(text)

常用方法
=======
checkbox.setText(text)

两态 (CheckBox 有两态和三态，两者不兼容)
======================================
checkbox.setChecked(True)
编程设置选中/未选中。

checkbox.isChecked()
检查选中还是未选中（只能用于两态）

三态 (CheckBox 有两态和三态，两者不兼容)
======================================
checkbox.setTristate(tristate)
如果设置为 True，那么CheckBox 会在指示框上显示一条线；三态通常用来展示它不是上面两态的任何一个值。

checkbox.isTristate()
检查是否开启了三态

checkbox.checkState()
获取三态下的选中状态

checkbox.setCheckState(state)
设置三态下的状态，可以是以下值：
Qt.Unchecked -- 未选中
Qt.PartiallyChecked 部分选中
Qt.Checked 选中
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QCheckBox
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 QCheckBox")

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox1 = QCheckBox("Kestrel")
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 0, 0)

        self.checkbox2 = QCheckBox("Sparrowhawk")
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 1, 0)

        self.checkbox3 = QCheckBox("Hobby")
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 2, 0)

        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2, 0, 1)
        layout.setHorizontalSpacing(5)

        self.checkbox4 = QCheckBox("Sex")
        self.checkbox4.setTristate(True)
        self.checkbox4.setCheckState(True)
        self.checkbox4.toggled.connect(self.checkbox_toggled)
        layout2.addWidget(self.checkbox4)

        self.checkbox5 = QCheckBox("Age")
        self.checkbox5.setTristate(False)
        self.checkbox5.setChecked(True)
        self.checkbox5.toggled.connect(self.checkbox_toggled)
        layout2.addWidget(self.checkbox5)

    def checkbox_toggled(self):
        selected = []

        print("\n")
        if self.checkbox1.isChecked():
            selected.append(self.checkbox1.text())

        if self.checkbox2.isChecked():
            selected.append(self.checkbox2.text())

        if self.checkbox3.isChecked():
            selected.append(self.checkbox3.text())

        if self.checkbox4.isTristate():
            if self.checkbox4.checkState() == Qt.PartiallyChecked:
                print("按钮4 -- 三态复选框 -- 部分选中了")
            elif self.checkbox4.checkState() == Qt.Unchecked:
                print("按钮4 -- 三态复选框 -- 取消选中")
            elif self.checkbox4.checkState() == Qt.Checked:
                print("按钮4 -- 三态复选框 -- 选中了")

        if self.checkbox5.isTristate():
            print("按钮5 -- 三态")
        else:
            if self.checkbox5.isChecked():
                print("按钮5 -- 非三态 -- 选中")
            else:
                print("按钮5 -- 非三态 -- 未选中")

        print("Selected: %s" % (" ".join(selected)))

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


