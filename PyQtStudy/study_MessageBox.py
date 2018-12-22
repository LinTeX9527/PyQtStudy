#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-22 18:56:40

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QMessageBox, QLabel, QPushButton, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

"""
QMessageBox 的几种常规用法，弹窗提示某些信息，用户通过按钮与之交互。

QMessageBox.information()

QMessageBox.question()

也可以实例化对象，设置图标，加载图片

"""


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 MessageBox")

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        gridlayout = QGridLayout()
        row_index = 0
        column_index = 0
        rowspan = 1
        columnspan = 1

        self.btn_info = QPushButton("Information")
        self.btn_question = QPushButton("Question")
        self.btn_warning = QPushButton("Warning")
        self.btn_critical = QPushButton("Critical")
        self.btn_about = QPushButton("About")
        self.btn_aboutqt = QPushButton("About Qt")

        gridlayout.setHorizontalSpacing(10)
        gridlayout.setVerticalSpacing(5)
        gridlayout.addWidget(self.btn_info, row_index, column_index, rowspan, columnspan)
        column_index += 1
        gridlayout.addWidget(self.btn_question, row_index, column_index, rowspan, columnspan)
        column_index += 1
        gridlayout.addWidget(self.btn_warning, row_index, column_index, rowspan, columnspan)
        # 开始下一行
        row_index += 1
        column_index = 0
        gridlayout.addWidget(self.btn_critical, row_index, column_index, rowspan, columnspan)
        column_index += 1
        gridlayout.addWidget(self.btn_about, row_index, column_index, rowspan, columnspan)
        column_index += 1
        gridlayout.addWidget(self.btn_aboutqt, row_index, column_index, rowspan, columnspan)

        # 开始下一行
        row_index += 1
        column_index = 0
        rowspan = 1
        columnspan = 3

        mainLayout.addLayout(gridlayout, 1)
        mainLayout.addStretch(1)
        self.lbl_msg = QLabel("在这里显示操作的结果")
        self.lbl_msg.setMaximumHeight(30)
        self.lbl_msg.setAlignment(Qt.AlignCenter)
        # gridlayout.addWidget(self.lbl_msg, row_index, column_index, rowspan, columnspan)
        mainLayout.addWidget(self.lbl_msg)
        mainLayout.addStretch(1)

        self.btn_info.clicked.connect(self.on_info)
        self.btn_question.clicked.connect(self.on_question)
        self.btn_warning.clicked.connect(self.on_warning)
        self.btn_critical.clicked.connect(self.on_critical)
        self.btn_about.clicked.connect(self.on_about)
        self.btn_aboutqt.clicked.connect(self.on_aboutQt)

    def update_choose_result(self, msg):
        self.lbl_msg.setText(msg)

    def on_info(self):
        reply = QMessageBox.information(self, "提示", "这是一个information对话框", QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.update_choose_result("你选择了Ok")
        else:
            self.update_choose_result("你选择了 Close")

    def on_question(self):
        reply = QMessageBox.question(self, "询问", "这是一个question对话框，默认是 No", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.update_choose_result("你选择了 Yes")
        elif reply == QMessageBox.No:
            self.update_choose_result("你选择了 No")
        else:
            self.update_choose_result("你选择了 Cancel")

    def on_warning(self):
        cb = QCheckBox("所有文档都按此操作")
        msgBox = QMessageBox()
        msgBox.setWindowTitle("警告")
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("这是一个 warning 对话框")
        msgBox.setInformativeText("是否愿意保存更改？")
        save = msgBox.addButton("保存", QMessageBox.AcceptRole)
        nosave = msgBox.addButton("取消", QMessageBox.RejectRole)
        cancel = msgBox.addButton("不保存", QMessageBox.DestructiveRole)
        msgBox.setDefaultButton(save)
        msgBox.setCheckBox(cb)
        cb.stateChanged.connect(self.on_check)
        reply = msgBox.exec()
        if reply == QMessageBox.AcceptRole:
            self.update_choose_result("你选择了保存")
        elif reply == QMessageBox.RejectRole:
            self.update_choose_result("你选择了取消")
        else:
            self.update_choose_result("你选择了不保存")

    def on_critical(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("严重错误")
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("这是一个 critial 对话框")
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setDetailedText("这是详细的信息：你需要更加努力，你已经落后了")
        reply = msgBox.exec()

        if reply == QMessageBox.Retry:
            self.update_choose_result("你选择了 Retry")
        elif reply == QMessageBox.Abort:
            self.update_choose_result("你选择了 Abort")
        else:
            self.update_choose_result("你选择了忽略这条消息")

    def on_about(self):
        msgBox = QMessageBox(QMessageBox.NoIcon, "关于", "不要做白日梦了，早点洗洗睡吧!")
        msgBox.setIconPixmap(QPixmap("./images/logo.png"))
        msgBox.exec()

    def on_aboutQt(self):
        QMessageBox.aboutQt(self, "关于Qt")

    def on_check(self):
        if self.sender().isChecked():
            self.update_choose_result("你打钩了")
        else:
            self.update_choose_result("怎么取消了打勾")

    def initGUI(self, title):
        """
        设置窗口大小和位置，以及标题
        """
        self.move(600, 350)
        self.setMinimumSize(300, 200)
        self.setWindowTitle(title)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen = MyWindow()
    screen.show()

    sys.exit(app.exec_())
