#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-18 14:13:27

@author: lintex9527@yeah.net
"""

"""
Slider 滑动条，很适合用来改变输出数值，例如调试麦克风的音量，屏幕的亮度等。

构造方法
=======
slider = QSlider(orientation)
可以选择的方向是：
Qt.Vertical
Qt.Horizontal

常用方法
========
slider.setOrientation(orientation)

slider.setMinimum(value)
slider.setMaximum(value)
默认的取值范围是0~99，可以通过这两个函数自定义。

slider.setValue(value)
设定滑动条当前的取值。如果取值超出了范围，控件会自动调节落在设定的取值范围内。

slider.setTracking(True/False)
默认情况下，滑动条在开始滑动、停止滑动时会发出信号通知用户滑动条的值已经改变了，
但是某些情况下需要跟踪滑动条，只要滑动条移动就会发出信号，这里需要设置为True。

slider.setTickInterval(interval)
滑动条上标注刻度的间隔。

slider.setTickPosition(position)
设置滑动条刻度值显示的位置，可以是如下值：
QSlider.NoTicks    -- 不显示刻度值
QSlider.TicksBothSides -- 两侧都显示刻度值
QSlider.TicksAbove -- 在水平方向的上面显示
QSlider.TicksBelow -- 在水平方向的下面显示
QSlider.TicksLeft  -- 在垂直方向的左侧显示
QSlider.TicksRight -- 在垂直方向的右侧显示
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QSlider
from PyQt5.QtCore import Qt
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 QSlider")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        slider = QSlider(Qt.Horizontal)
        slider.setValue(4)
        mainLayout.addWidget(slider, 0, 0)

        slider = QSlider(Qt.Vertical)
        slider.setValue(4)
        mainLayout.addWidget(slider, 0, 1)

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
