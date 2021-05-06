#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow,
                             qApp, QAction, QGridLayout, QGroupBox, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import settings as s
import general_draw_module as dm
import general_loop_module as lm


def generate_custom_pos():
    emptyDict = {}
    # print('custom pos generation started')
    for n in s.graph.nodes:
        try:
            if s.graph.nodes[n]['pos'] == 'None' or s.graph.nodes[n]['pos'] is None:
                print(str(n) + ' _node has no pos, set it up properly')
                print(str(n) + ' has invalid position, using default layout')
                s.draw_style = 'default'
                emptyDict = s.nx.planar_layout(s.graph)
                return emptyDict
            else:
                loc_arr = str(s.graph.nodes[n]['pos']).split(';')
                emptyDict[n] = [round(float(loc_arr[0]), 4), round(float(loc_arr[1]), 4)]
        except Exception as e:
            print(str(n) + ' has invalid position, using default layout(exception)')
            s.draw_style = 'default'
            emptyDict = s.nx.planar_layout(s.graph)
            return emptyDict
    # print('result of custom generation:')
    # print(emptyDict)
    return emptyDict


class Example(QMainWindow):
    NumButtons = ['plot1', 'plot2', 'plot3']

    def __init__(self):
        super().__init__()
        self.initUI()

    def local_draw_graph(self):
        self.figure.clf()
        colors = [s.graph.nodes[a].get('color', s.default_node_color) for a in s.graph.nodes]
        # please tell me why exactly colors work this way, but weights not
        # and why the way weight work colors don't want to?!

        if s.draw_style == 'default' or s.draw_style == 'planar':
            pos = s.nx.planar_layout(s.graph)
        elif s.draw_style == 'shell':
            pos = s.nx.shell_layout(s.graph)
        elif s.draw_style == 'spring':
            pos = s.nx.spring_layout(s.graph)
        elif s.draw_style == 'spectral':
            pos = s.nx.spectral_layout(s.graph)
        elif s.draw_style == 'none':
            pos = generate_custom_pos()
            # print('Selected none drawstyle. Make sure to set up all node positions!')
        elif s.draw_style == 'random':
            pos = s.nx.random_layout(s.graph)
        elif s.draw_style == 'circular':
            pos = s.nx.circular_layout(s.graph)
        else:
            print(
                'Hard switch to planar. What is this draw style? ' + s.draw_style + '; Please define a valid one (see help).')
            pos = s.nx.planar_layout(s.graph)

        # print('position from generated pos (' + str(s.draw_style) + ")")
        # print(pos)
        # for n in s.graph.nodes:
        #     print(str(s.graph.nodes[n]['pos']))
        # print(pos)
        if s.background_is_image:
            implot = s.plt.imshow(s.background_img)

        # if s.ax is None:
        #     s.fig, s.ax = s.plt.subplots()
        # s.graph.add_nodes_from(pos.keys()) # why is it here? it represents nothing.
        s.nx.draw(s.graph, pos, node_color=colors)
        labels = s.nx.get_edge_attributes(s.graph, 'weight')
        nd_labels = s.nx.get_node_attributes(s.graph, 'name')
        if s.show_weight_labels:
            s.nx.draw_networkx_edge_labels(s.graph, pos, edge_labels=labels)
        s.nx.draw_networkx_labels(s.graph, pos, labels=nd_labels)

        # test feature to get fullscreen
        mng = s.plt.get_current_fig_manager()
        if s.fullscreen:
            mng.window.state('zoomed')
        elif not s.fullscreen:
            pass
        self.canvas.draw_idle()


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
        menubar = self.menuBar()
        # now THIS creates a menu btn File, but it does nothing y yet
        fileMenu = menubar.addMenu('&File')
        # this adds an option, allows to leave and shows the shortcut
        fileMenu.addAction(exitAction)

        grid = QGridLayout()
        self.setLayout(grid)
        self.createVerticalGroupBox()

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.verticalGroupBox)

        self.figure = s.plt.gcf()
        self.canvas = FigureCanvas(self.figure)

        grid.addWidget(self.canvas, 0, 1, 9, 9)
        grid.addLayout(buttonLayout, 0, 0)

        dm.import_png('import riscani.png')
        dm.import_json('import mediumriscani-04-25-2021--19-21-43.json')
        self.local_draw_graph()

        # obligatory func
        self.show()

    def createVerticalGroupBox(self):
        self.verticalGroupBox = QGroupBox()

        layout = QVBoxLayout()
        for i in self.NumButtons:
            button = QPushButton(i)
            button.setObjectName(i)
            layout.addWidget(button)
            layout.setSpacing(10)
            self.verticalGroupBox.setLayout(layout)
            button.clicked.connect(lambda: print('hoi '+str(button.objectName())))

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
