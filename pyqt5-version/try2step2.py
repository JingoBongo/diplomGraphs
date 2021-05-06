#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow,
                             qApp, QAction)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

v = 5


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        # this is a rectangle responsible for the size of the screen
        qr = self.frameGeometry()
        # get central point of our screen resolution
        cp = QDesktopWidget().availableGeometry().center()
        # we move the rectangle to the center
        qr.moveCenter(cp)
        # qr is a rectangle, so we move top left corner of the app to the top left corner of rectangle
        self.move(qr.topLeft())

    def initUI(self):
        # set x, y and window size
        # self.setGeometry(300, 300, 300, 220)
        # same window params, but window is not centered. function is ours
        self.resize(300, 220)
        self.center()
        self.setWindowTitle('SP Finder')
        # set icon
        self.setWindowIcon(QIcon('icon.png'))
        # whatever tooltip is;;; всплывающая подсказка
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        # button stuff
        btn = QPushButton('Button', self)

        btn.setToolTip('This is a variable tooltip ' + str(v))
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # quit options
        qbtn = QPushButton('Print v++', self)
        # qbtn.clicked.connect(QCoreApplication.instance().quit)  # this will connect button to function exit it seems
        qbtn.clicked.connect(lambda: change_v())  # this will connect button to function exit it seems
        # yes, it does. but the tooltip doesnt update with the variable update. i guess init gui is called only once
        # to properly use it with arguments: use lambda as above
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 30)

        self.show()

    # but i didnt EVER connect this method to initgui or others. Predefined function name it seems
    def closeEvent(self, event):
        # so it is the popup, arguments are self0, text1, options(predefined, with |)2, highlighted option3.
        # doesnt react to button close app
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def change_v():
    global v
    v += 1
    print(v)


# this is probably a main starter, to say so
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # this is literally the class we created, so be nice to it
    ex = Example()
    sys.exit(app.exec_())
