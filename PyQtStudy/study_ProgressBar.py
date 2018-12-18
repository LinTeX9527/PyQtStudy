#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-18 19:46:20

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.QtWidgets import QProgressBar, QPushButton
from PyQt5.QtCore import Qt
import sys

"""
ProgressBar 显示进程完成情况。

构造方法
=======
progressbar = QProgressBar()

常用方法
=======
progressbar.setMinimum(value)
progressbar.setMaximum(value)
设置最大最小的值

int progressbar.minimum()
int progressbar.maximum()
取得最大最小值

int progressbar.value()
返回当前值

progressbar.setValue(int value)
设置当前进度值

progressbar.setOrientation(orientation)
设置进度条的显示方向，可以是如下值：
Qt.Horizontal
Qt.Vertical
默认的进度增长方向是： Horizontal 进度条 从左到右
Vertical 的进度条 从上到下

progressbar.setInvertAppearnce(True/False)
True 进度条增长方向设置为默认的相反方向
False 不变

progressbar.setTextVisible(True/False)
当前完成的百分比数值是否可见

progressbar.setFormat(format)
设置进度条完成百分比的显示格式，只能是如下的三者之一：
"%p" -- 百分比形式 30%
"%v" -- 数值形式 30
"%m" -- 步进个数

"""


class MyWindow(QWidget):
    """
    简单的 ProgressBar 演示
    TODO: 应该子线程线程处理事务，在主线程中更新GUI
    """
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 ProgressBar")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        # GUI 简图
        # -------------- 90% [增加] [复位]
        self.progress = QProgressBar()
        self.progress.setOrientation(Qt.Horizontal)
        self.progress.setMinimum(0)
        self.progress.setMaximum(99)
        self.progress_step = 5
        self.progress.setValue(80)
        mainLayout.addWidget(self.progress, 0, 0, 1, 2)

        btn_add = QPushButton("增加")
        btn_add.clicked.connect(self.on_add_clicked)
        mainLayout.addWidget(btn_add, 1, 0, 1, 1)

        btn_reset = QPushButton("复位")
        btn_reset.clicked.connect(self.on_reset_clicked)
        mainLayout.addWidget(btn_reset, 1, 1, 1, 1)

    def on_add_clicked(self):
        newValue = self.progress.value() + self.progress_step
        if newValue >= self.progress.maximum():
            newValue = self.progress.maximum()
        self.progress.setValue(newValue)

    def on_reset_clicked(self):
        self.progress.reset()

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
