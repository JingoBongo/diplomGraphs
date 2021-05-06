from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import general_draw_module as dm
import general_loop_module as lm
import general_alg_module as am
import settings as s


def choose_import(raw_input: str):
    if '.json' in raw_input:
        dm.import_json(raw_input)
    elif '.gexf' in raw_input:
        dm.import_gexf(raw_input)
    elif '.png' in raw_input:
        dm.import_png(raw_input)
    else:
        print('What is the file format from command? I accept .png, .gexf and .json: ' + str(raw_input))


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
        draw_graph_action.triggered.connect(self.draw_graph)
        return draw_graph_action

    def create_toggle_text_action(self):
        toggle_text_action = QAction('&Toggle Output', self)
        toggle_text_action.setShortcut('Ctrl+O')
        toggle_text_action.setStatusTip('Toggle Output')
        toggle_text_action.triggered.connect(self.toggle_console)
        return toggle_text_action

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
            print(str(fileName))
            lm.choose_import('import '+str(fileName))

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.center()
        self.setWindowTitle('S Plot')
        self.setWindowTitle('SP Finder')
        self.setWindowIcon(QIcon('icon.png'))

        grid = QGridLayout()
        self.setLayout(grid)

        # this is making useless buttons
        # self.createVerticalGroupBox()

        # so THIS creates a menubar, but it is empty
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
        file_menu.addAction(self.create_import_action())
        graph_menu.addAction(self.create_draw_graph_action())
        actions_menu.addAction(self.create_toggle_text_action())
        # adding all the menus.


        # buttonLayout = QHBoxLayout()
        # buttonLayout.addWidget(self.verticalGroupBox)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gui()
        # grid.addLayout(buttonLayout, 1, 0)
        grid.addWidget(self.canvas, 1, 0)
        self.argtextbox = QLineEdit(self)
        grid.addWidget(self.argtextbox, 2,0)

        # text console output
        self.console_output = QTextBrowser(self)
        self.console_output.setGeometry(QRect(10, 90, 331, 111))
        self.console_output.setObjectName("output")
        grid.addWidget(self.console_output, 1, 1)

        self.argtextbox.returnPressed.connect(lambda: lm.process_raw_input(self.argtextbox.text()))
        # self.execute_button = QPushButton('Execute')
        # self.execute_button.setObjectName('Execute')
        # self.execute_button.clicked.connect(lambda: lm.process_raw_input())
        # grid.addWidget(self.execute_button, 2, 1)
        self.show()

    def on_enter_pressed_behavior(self):
        lm.process_raw_input(self.argtextbox.text())
        self.console_output.append()

    def process_raw_input(self, raw_input: str):
        if 'help' in raw_input:
            help()
        elif 'add node' in raw_input:
            dm.add_node(raw_input)
        elif 'show weights' in raw_input:
            dm.show_edge_weights(raw_input)
        elif 'swap colors' in raw_input:
            dm.swap_colors(raw_input)
        elif 'add pnode' in raw_input:
            dm.add_posed_node(raw_input)
        elif 'drawstyle' in raw_input and 'print' not in raw_input:
            dm.define_draw_style(raw_input)
        elif 'add edge' in raw_input:
            dm.add_edge(raw_input)
        elif 'set npos' in raw_input:
            dm.set_node_pos(raw_input)
        # elif 'set nname' in raw_input:    buggy. there are workarounds
        #     dm.set_node_name(raw_input)
        elif 'set edge weight' in raw_input:
            dm.set_edge_weight(raw_input)
        elif 'convert' in raw_input:
            dm.convert(raw_input)
        elif 'get node dist' in raw_input:
            dm.get_node_dist(raw_input)
        elif 'get dist' in raw_input:  # 0get 1dist 2x1 3y1 4x2 5y2
            gda = raw_input.split(' ')
            if len(gda) == 5:
                dm.get_dist_between_two_points(gda[2], gda[3], gda[4], gda[5])
            else:
                print('improper command when getting dist from x1, y1, x2, y2')
        elif 'set weight proportion' in raw_input:  # set weight proportion u v xxxMetres
            dm.set_weight_proportion(raw_input)
        elif 'remove node' in raw_input:
            dm.remove_node(raw_input)
        elif 'fullscreen' in raw_input:
            dm.fullscreen(raw_input)
        elif 'remove edge' in raw_input:
            dm.remove_edge(raw_input)
        elif 'add bidirectional edge' in raw_input:
            dm.add_b_edge(raw_input)
        elif 'reset plot' in raw_input:
            dm.reset_plot()
        elif 'save image' in raw_input:
            dm.save_image(raw_input)
        elif 'save json' in raw_input:
            dm.save_json(raw_input)
        elif 'save gexf' in raw_input:
            dm.save_gexf(raw_input)
        elif 'pause' in raw_input:  # this allows us to return to working plot
            s.plt.clf()
            dm.gui()
            dm.draw_graph()
            s.plt.show(block=True)  # this alone can bring me back to plot when its closed
        elif 'ion' in raw_input:  # currently brings back
            s.plt.show()
            s.plt.ion()
        elif 'ioff' in raw_input:
            s.plt.ioff()
        elif 'draw' in raw_input:
            dm.draw_graph()
        elif 'show' in raw_input:
            s.plt.show()
        elif 'freeze' in raw_input:  # this really works if we want just the visuals while coding
            s.plt.clf()
            dm.draw_graph()
            s.plt.show()
            s.plt.ion()
            s.plt.pause(0.001)
        elif 'import' in raw_input:
            # if '.json' in raw_input:
            #     dm.import_json(raw_input)
            # elif '.gexf' in raw_input:
            #     dm.import_gexf(raw_input)
            # elif '.png' in raw_input:
            #     dm.import_png(raw_input)
            choose_import(raw_input)
        elif 'set node color' in raw_input:
            dm.change_node_color(raw_input)
        # elif 'enable plot' in raw_input or 'disable plot' in raw_input:
        #     dm.plot_enabler(raw_input)
        elif 'print' in raw_input:
            dm.print_list(raw_input)
        elif 'floyd' in raw_input:
            am.dum_dum_floyd_alg()
        elif 'shmoys' in raw_input:
            if len(raw_input.split(' ')) == 4:  # shmoys wh rad startingNode
                am.dum_dum_shmoys(raw_input.split(' ')[1], raw_input.split(' ')[2], raw_input.split(' ')[3])
            else:
                print('Improper usage of \'shmoys\' command, type help to get some clue')
        elif 'exit' in raw_input:
            s.whileBool = False
            print('Closing everything')
            s.plt.close()
        elif 'change graph type' in raw_input:
            graph_type = input('Please specify graph type(graph/digraph): >>')
            dm.process_graph_type(graph_type)
        else:
            print('Command not recognized: ' + raw_input)

    def gui(self):
        self.canvas.mpl_connect('button_release_event', self.on_click)
        # self.canvas.mpl_connect('key_release_event', self.release)

    def release(self, event):
        # print('press', event.key)
        # if event.key == 'x':
        #     print('it was the X spot')
        pass

    def on_click(self, event):
        if event.dblclick:
            print('doubleclick')
            # s.plt.ion()
            # s.plt.pause(0.01)
        if event.button:
            # print('click actually worked '+ str(event.xdata)+' '+str(event.ydata))
            # print('button clicked: '+str(event.button))
            if event.button == 3:
                round(float(event.xdata), 4)
                dm.add_posed_node('add pnode ' + s.generic_node_name + str(s.generic_node_name_counter) + ' ' + str(
                    round(float(event.xdata), 4)) + ' ' + str(round(float(event.ydata), 4)))
                s.generic_node_name_counter += 1
                self.draw_graph()
                # s.plt.show()
            if event.button == 2:
                # print('inside middle')
                try:
                    for n in s.graph.nodes:
                        npos = s.graph.nodes[n]['pos']
                        nx = float(str(npos).split(';')[0])
                        ny = float(str(npos).split(';')[1])
                        if dm.get_dist_between_two_points(round(float(event.xdata), 4), round(float(event.ydata), 4), nx,
                                                       ny) <= 15:
                            s.mouse_clicked_nodes.append(n)
                            break
                    if len(s.mouse_clicked_nodes) >= 2:
                        n1x = str(s.graph.nodes[str(s.mouse_clicked_nodes[0])]['pos']).split(';')[0]
                        n1y = str(s.graph.nodes[str(s.mouse_clicked_nodes[0])]['pos']).split(';')[1]
                        n2x = str(s.graph.nodes[str(s.mouse_clicked_nodes[1])]['pos']).split(';')[0]
                        n2y = str(s.graph.nodes[str(s.mouse_clicked_nodes[1])]['pos']).split(';')[1]
                        dist = dm.get_dist_between_two_points(n1x, n1y, n2x, n2y)
                        weight = float((float(s.prop_m) * float(dist)) / float(s.prop_d))
                        dm.add_edge('add edge ' + str(s.mouse_clicked_nodes[0]) + ' ' + str(
                            s.mouse_clicked_nodes[1]) + ' ' + str(weight))
                        s.mouse_clicked_nodes.clear()
                        self.draw_graph()
                        # s.plt.show()
                except Exception as e:
                    print('something went wrong while creating edge with mouse')
                    print(e)
            if event.button == 1:
                self.console_output.append('mouse pos: ' + str(event.xdata) + ' ' + str(event.ydata))
                print('mouse pos: ' + str(event.xdata) + ' ' + str(event.ydata))


    def createVerticalGroupBox(self):
        self.verticalGroupBox = QGroupBox()

        layout = QHBoxLayout()
        for i in  self.NumButtons:
                button = QPushButton(i)
                button.setObjectName(i)
                layout.addWidget(button)
                layout.setSpacing(10)
                self.verticalGroupBox.setLayout(layout)
                button.clicked.connect(lambda: (print(str(self.sender().objectName())), self.submitCommand()))

    def submitCommand(self):
        eval('self.' + str(self.sender().objectName()) + '()')



    def draw_graph(self):
        self.figure.clf()
        # dm.import_png('import riscani.png')
        # dm.import_json('import mediumriscani-04-25-2021--19-21-43.json')
        colors = [s.graph.nodes[a].get('color', s.default_node_color) for a in s.graph.nodes]
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
        elif s.draw_style == 'random':
            pos = s.nx.random_layout(s.graph)
        elif s.draw_style == 'circular':
            pos = s.nx.circular_layout(s.graph)
        else:
            print(
                'Hard switch to planar. What is this draw style? ' + s.draw_style + '; Please define a valid one (see help).')
            pos = s.nx.planar_layout(s.graph)

        if s.background_is_image:
            implot = s.plt.imshow(s.background_img)

        s.nx.draw(s.graph, pos, node_color=colors)
        labels = s.nx.get_edge_attributes(s.graph, 'weight')
        nd_labels = s.nx.get_node_attributes(s.graph, 'name')
        if s.show_weight_labels:
            s.nx.draw_networkx_edge_labels(s.graph, pos, edge_labels=labels)
        s.nx.draw_networkx_labels(s.graph, pos, labels=nd_labels)

        mng = s.plt.get_current_fig_manager()
        if s.fullscreen:
            mng.window.state('zoomed')
        elif not s.fullscreen:
            pass
        self.canvas.draw_idle()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


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

if __name__ == '__main__':

    import sys  
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = PrettyWidget() 
    screen.show()   
    sys.exit(app.exec_())