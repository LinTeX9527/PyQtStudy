#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create on 2018-12-17 17:55:58

@author: lintex9527@yeah.net
"""

"""
PushButton 用于用户交互，单击按钮时触发一个事件，开始下载或者删除文件。

构造方法
=======
pushbutton = QPushButton(text)

常用方法
=======
pushbutton.setText(text)

pushbutton.setFlat(True)
默认情况下按钮的四周稍微凸起一点点，可以调用这个方法设置为平的。

pushbutton.isFlat()
返回True/False，按钮是否是平的。

pushbutton.setMenu(menu)
按钮可以用来弹出菜单，而不仅仅是响应单击事件。

Signals
=======
pushbutton.clicked.connect(button_clicked_function)
连接信号与槽函数
"""

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI("QPushButton")
        # 按钮单击计数
        self.count = 0

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Click Me")
        # NOTE:为按钮添加单击响应事件
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 0, 0)

        self.label = QLabel("Message")
        layout.addWidget(self.label, 1, 0)

    def on_button_clicked(self):
        self.count += 1
        self.label.setText("按钮单击了%d次" % (self.count))

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

