from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import general_draw_module as dm
import general_loop_module as lm
import general_alg_module as am
import settings as s


class PrettyWidget(QWidget):

    def __init__(self):
        super(PrettyWidget, self).__init__()
        font = QFont()
        font.setPointSize(16)
        self.initUI()

    def create_exit_action(self):
        exitAction = QAction(QIcon("exit.png"), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        return exitAction

    def create_import_action(self):
        import_action = QAction('&Import', self)
        import_action.setShortcut('Ctrl+I')
        import_action.setStatusTip('Import file')
        import_action.triggered.connect(self.import_process)
        return import_action

    def create_draw_graph_action(self):
        draw_graph_action = QAction('&Draw Graph', self)
        draw_graph_action.setShortcut('Ctrl+D')
        draw_graph_action.setStatusTip('Draw Graph')
        draw_graph_action.triggered.connect(lambda: dm.draw_graph(self))
        # draw_graph_action.triggered.connect(lambda: self.draw_graph())
        return draw_graph_action

    def create_toggle_text_action(self):
        toggle_text_action = QAction('&Toggle Output', self)
        toggle_text_action.setShortcut('Ctrl+O')
        toggle_text_action.setStatusTip('Toggle Output')
        toggle_text_action.triggered.connect(self.toggle_console)
        return toggle_text_action

    def create_floyd_action(self):
        floyd_action = QAction('&Floyd Algorithm', self)
        floyd_action.setShortcut('Ctrl+F')
        floyd_action.setStatusTip('Floyd Algorithm')
        floyd_action.triggered.connect(lambda: am.dum_dum_floyd_alg(self))
        return floyd_action

    def create_generic_action(self, name, trigger_function, needs_arguments, description=None, shortcut=None):
        action = QAction('&' + str(name), self)
        action.setStatusTip(str(name))
        if shortcut:
            action.setShortcut(str(shortcut))
        action.triggered.connect(lambda: self.create_generic_trigger_func(trigger_function, needs_arguments, name, description))
        return action

    def create_generic_trigger_func(self, trigger_function, needs_arguments, name, description=None):
        if needs_arguments:
            desc = 'Please provide the arguments(separated by space):'
            if description:
                desc = description
            args, done1 = QInputDialog.getText(self, name, desc)
            if done1:
                trigger_function = trigger_function + ' ' + args
        lm.process_raw_input(self, trigger_function)

    def toggle_console(self):
        if self.console_output.isHidden():
            self.console_output.setHidden(False)
        else:
            self.console_output.setHidden(True)

    def import_process(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            # s.cust_print(self, ('importing '+str(fileName)))
            lm.process_raw_input(self, 'import ' + str(fileName))
            # lm.choose_import(self, ('import '+str(fileName)))
            # s.plt.imshow(fileName)

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.center()
        self.setWindowTitle('S Plot')
        self.setWindowTitle('SP Finder')
        self.setWindowIcon(QIcon('icon.png'))
        self.showMaximized()

        grid = QGridLayout()
        self.setLayout(grid)

        self.menubar = QMenuBar(self)
        self.menubar.setFixedHeight(25)
        grid.addWidget(self.menubar, 0, 0)
        # now THIS creates a menu btn File, but it does nothing y yet
        app_menu = self.menubar.addMenu('&App')
        file_menu = self.menubar.addMenu('&File')
        utils_menu = self.menubar.addMenu('&Utils')
        graph_menu = self.menubar.addMenu('&Graph')
        actions_menu = self.menubar.addMenu('&Actions')
        # this adds an option, allows to leave and shows the shortcut
        app_menu.addAction(self.create_exit_action())
        # file menu has import, save
        file_menu.addAction(self.create_import_action())
        file_menu.addAction(self.create_generic_action('Save graph', 'save', True, '[json/gexf/image] [new file name]'))
        # graph menu has draw, add, set, swap, remove functios
        graph_menu.addAction(self.create_draw_graph_action())
        graph_menu.addAction(self.create_generic_action('Add p-node', 'add pnode', True, '[nodename] [x coordinates] [y coordinates]'))
        graph_menu.addAction(self.create_generic_action('Add node', 'add node', True, '[nodename]'))
        graph_menu.addAction(self.create_generic_action('Add edge', 'add edge', True, '[node1] [node2] (weight)'))
        graph_menu.addAction(self.create_generic_action('Set node color', 'set node color', True, '[nodename] [color] ; please use standard colors.'))
        graph_menu.addAction(self.create_generic_action('Set node position', 'set npos', True, '[nodename] [x coordinates] [y coordinates]'))
        graph_menu.addAction(self.create_generic_action('Set edge weight', 'set edge weight', True, '[node1] [node2] (weight)'))
        graph_menu.addAction(self.create_generic_action('Swap colors', 'swap colors', True, '[color1] [color2]'))
        graph_menu.addAction(self.create_generic_action('Remove node', 'remove node', True, '[nodename]'))
        graph_menu.addAction(self.create_generic_action('Remove edge', 'remove edge', True, '[node1] [node2]'))
        # action menu has weight proportion, floyd, shmoys (+todo add cycles)... toggle?!...
        actions_menu.addAction(self.create_toggle_text_action())
        actions_menu.addAction(self.create_floyd_action())
        actions_menu.addAction(self.create_generic_action('Shmoys Algorithm', 'shmoys', True, '[warehouse nr.] [starting radius] [starting node/None]', shortcut='Ctrl+S'))
        actions_menu.addAction(self.create_generic_action('Cycled Shmoys Algorithm', 'cshmoys', True, '[warehouse nr.] [starting radius] [starting node/None] [cycles]'))
        actions_menu.addAction(self.create_generic_action('Set weight proportion', 'set weight proportion', True, '[node1] [node2] [actual distance]'))
        # utils menu. drawstyle, show weights,reset plot, prints, help, convert, get distances
        utils_menu.addAction(self.create_generic_action('Set drawstyle', 'drawstyle', True, '[planar/shell/spring/spectral/random/circular/none(preferred)]'))
        utils_menu.addAction(self.create_generic_action('Show edge weights', 'show weights', True, '[on/off]'))
        utils_menu.addAction(self.create_generic_action('Reset plot', 'reset plot', False, shortcut='Ctrl+R'))
        utils_menu.addAction(self.create_generic_action('Print node info', 'print one', True, '[nodename]'))
        utils_menu.addAction(self.create_generic_action('Print nodes info', 'print nodes', False))
        utils_menu.addAction(self.create_generic_action('Print edges info', 'print edges', False))
        utils_menu.addAction(self.create_generic_action('Print current drawstyle', 'print style', False))
        utils_menu.addAction(self.create_generic_action('Help (mostly for terminal)', 'help', False))
        utils_menu.addAction(self.create_generic_action('Convert distances', 'convert', True, '[coord dist/metric] [value]; example: convert__ dist 500'))
        # utils_menu.addAction(self.create_generic_action('Get distance between 2 points', 'get dist', True, '[x1 coordinates] [y1 coordinates] [x2 coordinates] [y2 coordinates]'))
        utils_menu.addAction(self.create_generic_action('Get distance between 2 nodes', 'get node dist', True, '[node1] [node2]'))
        # adding all the menus.

        self.figure = s.plt.figure()
        self.canvas = FigureCanvas(self.figure)
        dm.set_mouse_listener(self)
        # grid.addLayout(buttonLayout, 1, 0)
        grid.addWidget(self.canvas, 1, 0)
        self.argtextbox = QLineEdit(self)
        self.argtextbox.setFont(QFont('Arial', 12))
        grid.addWidget(self.argtextbox, 2, 0)

        # text console output
        self.console_output = QTextBrowser(self)
        self.console_output.setGeometry(QRect(10, 90, 331, 111))
        self.console_output.setObjectName("output")
        self.console_output.setFont(QFont('Arial', 12))
        self.console_output.setStyleSheet('background-color: grey;')
        grid.addWidget(self.console_output, 1, 1)
        self.console_output.setHidden(True)

        self.argtextbox.returnPressed.connect(self.on_enter_pressed_behavior)
        # self.execute_button = QPushButton('Execute')
        # self.execute_button.setObjectName('Execute')
        # self.execute_button.clicked.connect(lambda: lm.process_raw_input())
        # grid.addWidget(self.execute_button, 2, 1)
        self.show()

    def on_enter_pressed_behavior(self):
        s.cust_print(self, ('  '))
        s.cust_print(self, ('====/====/====/'))
        s.cust_print(self, ('  '))
        lm.process_raw_input(self, self.argtextbox.text())
        self.argtextbox.clear()

    def release(self, event):
        # s.cust_print(self, 'press', event.key)
        # if event.key == 'x':
        #     s.cust_print(self, 'it was the X spot')
        pass

    def createVerticalGroupBox(self):
        self.verticalGroupBox = QGroupBox()

        layout = QHBoxLayout()
        for i in self.NumButtons:
            button = QPushButton(i)
            button.setObjectName(i)
            layout.addWidget(button)
            layout.setSpacing(10)
            self.verticalGroupBox.setLayout(layout)
            button.clicked.connect(lambda: (s.cust_print(self, str(self.sender().objectName())), self.submitCommand()))

    def submitCommand(self):
        eval('self.' + str(self.sender().objectName()) + '()')



    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = PrettyWidget()
    screen.show()
    sys.exit(app.exec_())
