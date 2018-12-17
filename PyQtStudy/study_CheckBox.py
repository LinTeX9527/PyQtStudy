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

    def checkbox_toggled(self):
        selected = []

        if self.checkbox1.isChecked():
            selected.append(self.checkbox1.text())

        if self.checkbox2.isChecked():
            selected.append(self.checkbox2.text())

        if self.checkbox3.isChecked():
            selected.append(self.checkbox3.text())

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


