#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-22 16:52:20

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QFontDialog
from PyQt5.QtWidgets import QScrollArea, QTextEdit, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
import sys

"""
FileDialog 选择文件
ColorDialog 选取颜色
FontDialog 选择字体

构造方法
=======

常用方法
=======

最简单的用法
file_name = QFileDialog.getOpenFileName(self, caption="打开文件", start_dir='./')

# 选择颜色
newcolor = QColorDialog.getColor()
if newcolor.isValid():
    self.textedit.setTextColor(newcolor)


# 选择字体
font, ok = QFontDialog.getFont()
if ok:
    self.textedit.setCurrentFont(font)

"""


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 FileDialog ColorDialog FontDialog")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        scrollarea = QScrollArea(self)
        self.textedit = QTextEdit(self)
        self.textedit.setText("请在这里输入文字")
        self.textedit.setAlignment(Qt.AlignLeading)
        scrollarea.setWidget(self.textedit)
        scrollarea.setWidgetResizable(True)
        scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        mainLayout.addWidget(scrollarea, 0, 0, 3, 1)

        vbox = QVBoxLayout()
        self.btn_file = QPushButton("选择文本文件")
        self.btn_color = QPushButton("选择颜色")
        self.btn_font = QPushButton("选择字体")
        vbox.addWidget(self.btn_file)
        vbox.addWidget(self.btn_color)
        vbox.addWidget(self.btn_font)
        mainLayout.addLayout(vbox, 0, 1, 3, 1)

        # 为按钮绑定槽函数
        self.btn_file.clicked.connect(self.on_btn_clicked)
        self.btn_color.clicked.connect(self.on_btn_clicked)
        self.btn_font.clicked.connect(self.on_btn_clicked)

    def on_btn_clicked(self):
        sender = self.sender()
        if sender == self.btn_file:
            # 选择文件
            file_name = QFileDialog.getOpenFileName(self, "打开文件", './')
            if file_name[0]:
                with open(file_name[0], 'r', encoding='utf-8', errors='ignore') as f:
                    self.textedit.setText(f.read())
        elif sender == self.btn_color:
            # 选择颜色
            newcolor = QColorDialog.getColor()
            if newcolor.isValid():
                self.textedit.setTextColor(newcolor)
        elif sender == self.btn_font:
            # 选择字体
            font, ok = QFontDialog.getFont()
            if ok:
                self.textedit.setCurrentFont(font)

    def initGUI(self, title):
        """
        设置窗口大小和位置，以及标题
        """
        self.setMinimumSize(480, 320)
        self.setWindowTitle(title)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen = MyWindow()
    screen.show()

    sys.exit(app.exec_())
