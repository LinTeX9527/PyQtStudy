#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-22 17:56:25

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QFontDialog
from PyQt5.QtWidgets import QScrollArea, QTextEdit, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QDialog
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter
from PyQt5.QtCore import Qt
import sys

"""
FileDialog 选择文件
ColorDialog 选取颜色
FontDialog 选择字体

打印相关的类
===========
QPageSetupDialog -- 打印页面设置
QPrintDialog -- 打印设置
QPrinter -- 抽象的打印机

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
        self.initGUI("PyQt5 学习 PrintDialog Printer")

        # NOTE: 注意这里要先获得一个打印机
        self.printer = QPrinter()

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
        self.btn_openOneFile = QPushButton("选择文本文件")
        self.btn_openMultipleFile = QPushButton("打开多个文件")
        self.btn_saveFile = QPushButton("保存文件")
        self.btn_color = QPushButton("选择颜色")
        self.btn_font = QPushButton("选择字体")
        self.btn_pagesetting = QPushButton("页面设置")
        self.btn_printdialog = QPushButton("打印文档")
        vbox.addWidget(self.btn_openOneFile)
        vbox.addWidget(self.btn_openMultipleFile)
        vbox.addWidget(self.btn_saveFile)
        vbox.addWidget(self.btn_color)
        vbox.addWidget(self.btn_font)
        vbox.addWidget(self.btn_pagesetting)
        vbox.addWidget(self.btn_printdialog)
        mainLayout.addLayout(vbox, 0, 1, 3, 1)

        # 为按钮绑定槽函数
        self.btn_openOneFile.clicked.connect(self.on_btn_clicked)
        self.btn_openMultipleFile.clicked.connect(self.on_btn_clicked)
        self.btn_saveFile.clicked.connect(self.on_btn_clicked)
        self.btn_color.clicked.connect(self.on_btn_clicked)
        self.btn_font.clicked.connect(self.on_btn_clicked)
        self.btn_pagesetting.clicked.connect(self.on_btn_clicked)
        self.btn_printdialog.clicked.connect(self.on_btn_clicked)

    def on_btn_clicked(self):
        sender = self.sender()
        if sender == self.btn_openOneFile:
            # 选择文件
            file_name = QFileDialog.getOpenFileName(self, "打开文件", './')
            if file_name[0]:
                with open(file_name[0], 'r', encoding='utf-8', errors='ignore') as f:
                    self.textedit.setText(f.read())
        elif sender == self.btn_openMultipleFile:
            # 打开多个文件
            filenames = QFileDialog.getOpenFileNames(self, "打开多个文件", './')
            print(filenames)
            if filenames[0]:
                for fname in filenames[0]:
                    with open(fname, 'r', encoding="utf-8", errors='ignore') as f:
                        self.textedit.append(f.read())
        elif sender == self.btn_saveFile:
            filenames = QFileDialog.getSaveFileName(self, "保存文件", 'F:/temp/', "Text file(*.txt)")
            if filenames[0]:
                with open(filenames[0], 'w', encoding='utf-8', errors='ignore') as f:
                    f.write(self.textedit.toPlainText())
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
        elif sender == self.btn_pagesetting:
            # 打印页面设置
            pagesetting_dialog = QPageSetupDialog(self.printer, self)
            pagesetting_dialog.exec_()
        elif sender == self.btn_printdialog:
            # 打印开始执行
            print_dialog = QPrintDialog(self.printer, self)
            if QDialog.Accepted == print_dialog.exec_():
                self.textedit.print(self.printer)

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
