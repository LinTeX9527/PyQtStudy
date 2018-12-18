#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-18 16:57:59

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QDial
from PyQt5.QtCore import Qt
import sys

"""
Dial 外形像一个速度计或者拨号盘，和 Slider 非常相似。

构造方法
=======
dial = QDial()

常用方法
=======
dial.setMinimum(value)
dial.setMaximum(value)
dial.minimum()
dial.maximum()

dial.setValue(value)
dial.value()

dial.setWrapping(True/False)
默认情况下，Dial 在达到最大值时会跳到最小值，如果设置为False 就不会。

# NOTE: 最好不要启用 setNotchTarget()，因为默认样式就挺好的
dial.setNotchTarget(float)
凹槽之间的间隔，以像素点为单位，可以是浮点数。

# NOTE: 默认是不显示的，最好启用
dial.setNotchesVisible(True/False)
控制是否显示凹槽

signals 很重要
=============
void actionTriggered(int action)

void rangeChanged(int min, int max)

void sliderMoved(int value)

void sliderPressed()

void sliderReleased()

void valueChanged(int value)
"""


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 QDial")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(50)
        # 最好不要启用 setNotchTarget()，因为默认样式就挺好的
        # self.dial.setNotchTarget(10)
        self.dial.setNotchesVisible(True)
        self.dial.setWrapping(False)

        self.dial.sliderPressed.connect(self.on_slider_pressed_func)
        self.dial.sliderReleased.connect(self.on_slider_released_func)
        self.dial.sliderMoved.connect(self.on_slider_moved_func)
        self.dial.valueChanged.connect(self.on_value_changed)

        mainLayout.addWidget(self.dial, 0, 0, 1, 1)

    def on_slider_pressed_func(self):
        print("Dial --- Pressed")

    def on_slider_released_func(self):
        print("Dial --- Released @ %d" % (self.dial.value()))

    def on_slider_moved_func(self, value):
        print("Dial move to value = %d" % (value))

    def on_value_changed(self):
        print("Current dial value: %i" % (self.dial.value()))

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
