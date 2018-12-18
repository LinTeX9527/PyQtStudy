#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-18 18:00:12

@author: lintex9527@yeah.net
"""

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLCDNumber, QLabel
from PyQt5.QtCore import Qt
import sys

"""
LCDNumber 显示效果就行LCD屏幕一样，可以用作计算器、手表等。

构造方法
=======
lcdnumber = QLCDNumber()

常用方法
=======
lcdnumber.display(number)
lcdnumber.display(text)
设置显示内容，@number 可以是 integer 或者 float 数。

lcdnumber.value()
返回显示的文本。

lcdnumber.setBinMode()
lcdnumber.setOctMode()
lcdnumber.setDecMode()
lcdnumber.setHexMode()
设置显示的数值的模式

lcdnumber.setSmallDecimalPoint(True/False)
设置小数点是一丁点大，还是占据一个数字的大小

lcd_id.setDigitCount(number)
设置能显示的数字的最大个数
"""


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("PyQt5 学习 LCDNumber")

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        # 要展示的数据
        price = 13.568
        amount = 213
        id = "18726345"

        lbl_price = QLabel("价格:")
        lbl_amount = QLabel("数量：")
        lbl_id = QLabel("商品编号：")

        lcd_price = QLCDNumber()
        lcd_price.setDecMode()
        lcd_price.setSmallDecimalPoint(True)
        lcd_price.display(price)
        mainLayout.addWidget(lbl_price, 0, 0)
        mainLayout.addWidget(lcd_price, 0, 1, 1, 3)

        lcd_amount = QLCDNumber()
        lcd_amount.display(amount)
        mainLayout.addWidget(lbl_amount, 1, 0)
        mainLayout.addWidget(lcd_amount, 1, 1, 1, 3)

        lcd_id = QLCDNumber()
        lcd_id.setDecMode()
        # NOTE: 设置能显示的数字的最大个数，如果不设置大一点，有可能显示不完整
        lcd_id.setDigitCount(10)
        lcd_id.display(id)
        mainLayout.addWidget(lbl_id, 2, 0)
        mainLayout.addWidget(lcd_id, 2, 1, 1, 3)

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
