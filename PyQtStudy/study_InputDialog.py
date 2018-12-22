#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-22 14:11:54

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QInputDialog
from PyQt5.QtWidgets import QTextBrowser, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt
import sys

"""
PyQt5 工程模板

构造方法
=======
不需要使用构造方法，因为有5个常用的静态方法，直接获得用户输入的值。

常用方法
=======
5 个常用的静态方法，可以分别获取 int, str, double, item, multipleText值。
静态方法示例如下：

double_value, ok = QInputDialog.getDouble(QWidget &parent, str windowTitle, str prompt, min=最小值，max=最大值)
如果 ok == True 说明用户点击了确认按钮，返回值 double_value 是有效的

其他的方法调用方式是一样的。

double_value, ok = QInputDialog.getDouble()
int_value, ok = QInputDialog.getInt()
text, ok = QInputDialog.getItem(widget, winTitle, prompt, ['item1', 'item2', ...])
text, ok = QInputDialog.getText()
text, ok = QInputDialog.getMultipleText()

详细的参数列表参见Qt手册

"""


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 InputDialog")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)
        row = 0
        column = 0
        rowspan = 1
        columnspan = 1

        hbox_name = QHBoxLayout()
        lbl_name = QLabel("姓名：")
        self.ld_name = QLineEdit("")
        self.btn_name = QPushButton("修改姓名")
        hbox_name.addWidget(lbl_name)
        hbox_name.addWidget(self.ld_name)
        hbox_name.addWidget(self.btn_name)
        mainLayout.addLayout(hbox_name, row, column, rowspan, columnspan)
        row += 1

        hbox_age = QHBoxLayout()
        lbl_age = QLabel("年龄：")
        self.ld_age = QLineEdit("18")
        self.btn_age = QPushButton("修改年龄")
        hbox_age.addWidget(lbl_age)
        hbox_age.addWidget(self.ld_age)
        hbox_age.addWidget(self.btn_age)
        mainLayout.addLayout(hbox_age, row, column, rowspan, columnspan)
        row += 1

        hbox_sex = QHBoxLayout()
        lbl_sex = QLabel("性别：")
        self.ld_sex = QLineEdit("男")
        self.btn_sex = QPushButton("修改性别")
        hbox_sex.addWidget(lbl_sex)
        hbox_sex.addWidget(self.ld_sex)
        hbox_sex.addWidget(self.btn_sex)
        mainLayout.addLayout(hbox_sex, row, column, rowspan, columnspan)
        row += 1

        hbox_height = QHBoxLayout()
        lbl_height = QLabel("身高（cm）:")
        self.ld_height = QLineEdit("175")
        self.btn_height = QPushButton("修改身高")
        hbox_height.addWidget(lbl_height)
        hbox_height.addWidget(self.ld_height)
        hbox_height.addWidget(self.btn_height)
        mainLayout.addLayout(hbox_height, row, column, rowspan, columnspan)
        row += 1

        hbox_basicInfo = QHBoxLayout()
        lbl_basicInfo = QLabel("基本信息：")
        self.btn_basicInfo = QPushButton("修改信息")
        hbox_basicInfo.addWidget(lbl_basicInfo)
        hbox_basicInfo.addStretch(1)
        hbox_basicInfo.addWidget(self.btn_basicInfo)
        mainLayout.addLayout(hbox_basicInfo, row, column, rowspan, columnspan)
        row += 1

        self.text_browser = QTextBrowser()
        self.text_browser.setToolTip("个人基本信息")
        rowspan = 3
        columnspan = 3
        mainLayout.addWidget(self.text_browser, row, column, rowspan, columnspan)

        # 为所有的按钮连接槽函数
        self.btn_age.clicked.connect(self.showDialog)
        self.btn_basicInfo.clicked.connect(self.showDialog)
        self.btn_height.clicked.connect(self.showDialog)
        self.btn_name.clicked.connect(self.showDialog)
        self.btn_sex.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        sex = ['男', '女']
        if sender == self.btn_name:
            text, ok = QInputDialog.getText(self, "修改姓名", "请输入姓名：")
            if ok:
                self.ld_name.setText(text)
        elif sender == self.btn_age:
            text, ok = QInputDialog.getInt(self, "修改年龄", "请输入年龄：", min=1, max=130)
            if ok:
                self.ld_age.setText(str(text))
        elif sender == self.btn_sex:
            text, ok = QInputDialog.getItem(self, "修改性别", "请选择性别：", sex)
            if ok:
                self.ld_sex.setText(text)
        elif sender == self.btn_height:
            text, ok = QInputDialog.getDouble(self, "修改身高", "请输入身高：", min=1.0)
            if ok:
                self.ld_height.setText(str(text))
        elif sender == self.btn_basicInfo:
            text, ok = QInputDialog.getMultiLineText(self, "修改信息", "请输入个人信息：")
            if ok:
                self.text_browser.setText(text)

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
