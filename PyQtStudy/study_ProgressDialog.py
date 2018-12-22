#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-22 23:28:44

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QLabel, QPushButton, QProgressDialog, QMessageBox
from PyQt5.QtCore import Qt
import sys

"""
使用 ProgressDialog 提示用户操作要花费很长时间，且表明应用没有冻结。
它也可以给用户一个中止操作的机会。

进度对话框的一个常见问题是很难知道何时使用它们：操作在不同的硬件上花费的时间不同。
QProgressDialog 提供了一个解决方法：它估计操作所花费的时间（基于步骤的时间，
并且只有当该估计值超出 minimumDuration() (默认值为4秒)时才显示。

最主要的几个参数就是 minimum, maximum 和 value 当前值，通过这3个值来更新当前的
进度。


构造方法
=======
progress = QProgressDialog()
progress = QProgressDialog(labelText, cancelButtonText, minimu, maximum)

常用方法
=======
progress.setValue(value)
更新当前进度

progress.setAutoClose(True/False)

progress.setCancelButton(button)
添加一个自定义的按钮

progress.wasCanceled()
检查用户是否取消了操作

"""


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 ProgressDialog")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        lbl = QLabel("要复制的文件个数：")
        self.lineedit = QLineEdit("100000")
        self.lineedit.setMinimumWidth(100)
        self.btn_start = QPushButton("开始复制")
        self.btn_start.clicked.connect(self.show_dialog)

        row_index = 0
        column_index = 0
        mainLayout.addWidget(lbl, row_index, column_index)
        column_index += 1
        mainLayout.addWidget(self.lineedit, row_index, column_index)
        column_index += 1
        mainLayout.addWidget(self.btn_start, row_index, column_index)

    def show_dialog(self):
        num = int(self.lineedit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("操作执行中")
        progress.setLabelText("请稍候。。。")
        progress.setCancelButtonText("取消操作")
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, num)
        progress.setAutoClose(True)

        for i in range(num):
            progress.setValue(i)
            # NOTE: 在更新进程的过程中，如果检查到用户取消了，就需要退出这个更新进度的过程
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作中止")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")

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
