#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow,
                             qApp, QAction)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QMainWindow):

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
        self.center()
        self.resize(300, 220)
        self.setWindowTitle('SP Finder')
        self.setWindowIcon(QIcon('icon.png'))
        # action is the thing that will happen _if_. in this case if in menu bar you press on it
        exitAction = QAction(QIcon("exit.png"), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # menubar version
        # does it make a status bar already? nah. do i even need this? not sure
        # self.statusBar()
        # so THIS creates a menubar, but it is empty
        # menubar = self.menuBar()
        # now THIS creates a menu btn File, but it does nothing y yet
        # fileMenu = menubar.addMenu('&File')
        # this adds an option, allows to leave and shows the shortcut
        # fileMenu.addAction(exitAction)

        # toolbar version; this simple showed me the exit icon and seemed to create an upper line for other actions
        # I CAN MOVE THE ACTION.. omg i will not use this
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # obligatory func
        self.show()

    def closeEvent(self, event):
        # so it is the popup, arguments are self0, text1, options(predefined, with |)2, highlighted option3.
        # doesnt react to button close app
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # this is literally the class we created, so be nice to it
    ex = Example()
    sys.exit(app.exec_())
