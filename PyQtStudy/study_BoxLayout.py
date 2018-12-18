#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BoxLayout 和 GridLayout 相似，但是它只支持单个方向排列组件，可以动态地调整它包含的组件。

构造方法
=======
boxlayout = QBoxLayout()

设定方向
=======
boxlayout.setDirection(direction)

@direction 可以是以下值：
QBoxLayout.LeftToRight
QBoxLayout.RightToLeft
QBoxLayout.TopToBottom
QBoxLayout.BottomToTop

常用方法
=======
boxlayout.addWidget(widget, stretch, alignment)
boxlayout.insertWidget(index, widget, stretch, alignment)

@stretch integer 类型，指示子组件的伸展系数
@alignment 表示对齐方式，可以是以下值：
Qt.AlignLeft
Qt.AlignRight
Qt.AlignHCenter
Qt.AlignJustify

可以在 BoxLayout 中添加其他的布局管理器:
boxlayout.addLayout(layout, stretch)
boxlayout.insertLayout(index, layout, stretch)

指定每个子组件之间的像素间隔（默认值为0）
boxlayout.setSpacing(spacing)

boxlayout.addSpacing(spacing)
boxlayout.insertSpacing(index, spacing)
"""


from PyQt5.QtWidgets import QWidget, QBoxLayout, QLabel, QApplication, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        "另一种初始化方法"
        super(Window, self).__init__()

        self.initGUI("BoxLayout")

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        label = QLabel("C")
        layout.addWidget(label, 0)
        label = QLabel("C++")
        layout.addWidget(label, 0)

        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)

        label = QLabel("Java")
        layout2.addWidget(label, 0)
        label = QLabel("Python")
        layout2.addWidget(label, 0)

        # 新的布局，管理两个按钮
        layout3 = QBoxLayout(QBoxLayout.RightToLeft)
        layout.addLayout(layout3)

        # TODO: 给按钮添加响应方法
        btn_opacity_half = QPushButton("半透明")
        layout3.addWidget(btn_opacity_half)
        btn_opacity_all = QPushButton("完全不透明")
        layout3.addWidget(btn_opacity_all)


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

    screen = Window()
    screen.show()

    sys.exit(app.exec_())
