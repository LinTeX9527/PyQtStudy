#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-17 20:04:46

@author: lintex9527@yeah.net
"""

"""
LineEdit 接受单行输入，通常用来输入用户名或者密码

常用方法
=======
linedit.setText(text)
linedit.insert(text)
设置文本

linedit.text()
获取文本

lineedit.setPlaceholderText(text)
设置占位符，指示控件的意图 # NOTE：大概就是程序提示用户应该输入什么

lineedit.setReadOnly(True)
设置为只读，用户不能修改文本

lineedit.setMaxLength(length)
默认的文本长度是 32767 个字符，可以按照需求修改

lineedit.setCompleter(completer)
设置 Completer # NOTE: 有什么用


Signals 文本发生改变或者输入完成的信号
===================================

lineedit.returnPressed.connect(return_pressed_function)
用户完成输入，按下ENTER 或者 RETURN 键时发出一个信号

lineedit.textChanged.connect(text_changed_function)
只要里面的文本发生了改变就发出一个信号
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLineEdit, QLabel
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 LineEdit")

        layout = QGridLayout()
        self.setLayout(layout)

        self.lineedit = QLineEdit()
        # 绑定信号与槽函数
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineedit, 0, 0)

        self.msgBox = QLabel()
        self.msgBox.resize(100, 60)
        layout.addWidget(self.msgBox, 1, 0)

    def text_changed(self):
        """
        当输入框中文本发生变化时就触发这个方法
        """
        print(self.lineedit.text())

    def return_pressed(self):
        """
        当用户在LineEdit中完成输入时按下ENTER键或者RETURN键时就会触发这个函数
        """
        self.msgBox.setText(self.lineedit.text())

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
