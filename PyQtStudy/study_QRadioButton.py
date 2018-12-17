#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-17 18:12:06

@author: lintex9527@yeah.net
"""

"""
RadioButton 是单选按钮，多个QRadioButton组合但是一次只能选中其中的一个。

NOTE: 如果应用场景是一次能够选中多个按钮，请使用 CheckBox 或者 PushButton。

构造方法
=======
radiobutton = QRadioButton(text)

常用方法
=======
radiobutton.setText(text)
radiobutton.text()
设置文本、取回文本

radiobutton.setChecked(True)
设置是否选中，True -- 选中；False -- 不选中

radiobutton.isChecked()
检查是否选中

NOTE: 默认情况下窗口中的所有 RadioButton 都处于同一个组中，要想按照意图设置不同
的组别，需要使用 ButtonGroup 来设置。

radiobutton.setIcon(icon)
设置图标
"""

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QGridLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("QRadioButton")

        layout = QGridLayout()
        self.setLayout(layout)

        # RadioButton 设置，默认的所有的都是出于同一个按钮组
        rdbtn = QRadioButton("Brazil")
        rdbtn.setChecked(True)
        # NOTE: 可以绑定用户定义的数据
        rdbtn.country = "Brazil"
        rdbtn.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(rdbtn, 0, 0)

        rdbtn = QRadioButton("Argentian")
        rdbtn.country = "Argentian"
        # 连接信号与槽函数
        rdbtn.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(rdbtn, 0, 1)

        rdbtn = QRadioButton("Ecuador")
        rdbtn.country = "Ecuador"
        rdbtn.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(rdbtn, 0, 2)

    # NOTE: 注意槽函数的参数是 self
    def on_radio_button_toggled(self):
        # NOTE: 获取信号的发送者
        rdbtn = self.sender()

        if rdbtn.isChecked():
            print("Selected country is %s" % (rdbtn.country))

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
