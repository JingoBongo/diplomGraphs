import settings as s
import general_draw_module as dm
import general_alg_module as am


def choose_import(self, raw_input: str):
    if '.json' in raw_input:
        dm.import_json(self, raw_input)
    elif '.gexf' in raw_input:
        dm.import_gexf(self, raw_input)
    elif '.png' in raw_input:
        dm.import_png(self, raw_input)
    else:
        s.cust_print(self, ('What is the file format from command? I accept .png, .gexf and .json: ' + str(raw_input)))


def process_raw_input(self, raw_input: str):
    if 'help' in raw_input:
        help(self)
    elif 'cls' == raw_input:
        self.console_output.clear()
    elif 'import' in raw_input:
        choose_import(self, raw_input)
    elif 'add node' in raw_input:
        dm.add_node(self, raw_input)
    elif 'show weights' in raw_input:
        dm.show_edge_weights(self, raw_input)
    elif 'swap colors' in raw_input:
        dm.swap_colors(self, raw_input)
    elif 'add pnode' in raw_input:
        dm.add_posed_node(self, raw_input)
    elif 'drawstyle' in raw_input and 'print' not in raw_input:
        dm.define_draw_style(self, raw_input)
    elif 'add edge' in raw_input:
        dm.add_edge(self, raw_input)
    elif 'set npos' in raw_input:
        dm.set_node_pos(self, raw_input)
    elif 'set edge weight' in raw_input:
        dm.set_edge_weight(self, raw_input)
    elif 'convert' in raw_input:
        dm.convert(self, raw_input)
    elif 'get node dist' in raw_input:
        dm.get_node_dist(self, raw_input)
    elif 'get dist' in raw_input:  # 0get 1dist 2x1 3y1 4x2 5y2
        gda = raw_input.split(' ')
        if len(gda) == 6:
            dm.get_dist_between_two_points(self, gda[2], gda[3], gda[4], gda[5])
        else:
            s.cust_print(self, ('improper command when getting dist from x1, y1, x2, y2'))
    elif 'set weight proportion' in raw_input:  # set weight proportion u v xxxMetres
        dm.set_weight_proportion(self, raw_input)
    elif 'remove node' in raw_input:
        dm.remove_node(self, raw_input)
    elif 'remove edge' in raw_input:
        dm.remove_edge(self, raw_input)
    elif 'add bidirectional edge' in raw_input:
        dm.add_b_edge(self, raw_input)
    elif 'reset plot' in raw_input:
        dm.reset_plot()
    elif 'save image' in raw_input:
        dm.save_image(self, raw_input)
    elif 'save json' in raw_input:
        dm.save_json(self, raw_input)
    elif 'save gexf' in raw_input:
        dm.save_gexf(self, raw_input)
    elif 'draw' in raw_input:
        dm.draw_graph(self)
    elif 'set node color' in raw_input:
        dm.change_node_color(self, raw_input)
    elif 'print' in raw_input:
        dm.print_list(self, raw_input)
    elif 'floyd' in raw_input:
        am.dum_dum_floyd_alg(self)
    elif 'cshmoys' in raw_input:
        if len(raw_input.split(' ')) == 5:  # shmoys wh rad startingNode cycles
            am.dum_dum_shmoys_cycled(self, raw_input.split(' ')[1], raw_input.split(' ')[2], raw_input.split(' ')[3], raw_input.split(' ')[4])
        else:
            s.cust_print(self, ('Improper usage of \'shmoys\' command, type help to get some clue'))
    elif 'shmoys' in raw_input:
        if len(raw_input.split(' ')) == 4:  # shmoys wh rad startingNode
            am.dum_dum_shmoys(self, raw_input.split(' ')[1], raw_input.split(' ')[2], raw_input.split(' ')[3])
        else:
            s.cust_print(self, ('Improper usage of \'shmoys\' command, type help to get some clue'))
    else:
        s.cust_print(self, ('Command not recognized: ' + raw_input))
#         here, by the new logic I re-draw HERE. in case the command was successful. lets see how it goes
    if s.successfulCommand:
        s.successfulCommand = False
        dm.draw_graph(self)


def help(self):
    s.cust_print(self, ('commands are:'))
    s.cust_print(self, ('-===[ While canvas active: ]===-'))
    s.cust_print(self, ('left mouse click on plot: print mouse position'))
    s.cust_print(self, ('right mouse click on plot: create node at mouse position'))
    s.cust_print(self, ('middle mouse click on 2 nodes sequentially: create edge between specified nodes'))
    # s.cust_print(self, ('CTRL + W: close canvas'))
    s.cust_print(self, ('-===[ While terminal active: ]===-'))
    # s.cust_print(self, ('pause : pauses terminal and switches to canvas'))
    # s.cust_print(self, ('freeze : freezes canvas, leaving terminal active'))
    s.cust_print(self, ('import [path(if not from .py/.exe file folder) + filename] ; I accept .png, .gexf and .json'))
    s.cust_print(self, ('save image [image name] : saves just the image'))
    s.cust_print(self, ('save json [file name] : saves graph'))
    s.cust_print(self, ('save gexf [file name] : saves graph'))
    s.cust_print(self, ('add node [node_name] (possible node weight)'))
    s.cust_print(self, ('add pnode [node_name] (possible node weight) [x coordinates] [y coordinates]'))
    s.cust_print(self, ('add edge [1st node name] [2nd node name] (possible edge weight)'))
    s.cust_print(self, ('set node color [node name] [color]'))
    s.cust_print(self, ('swap colors [color1] [color2] : replaces color1 with color2'))
    s.cust_print(self, ('set edge weight [u] [v] [weight]'))
    s.cust_print(self, ('set weight proportion [u] [v] [metric value] : sets distance between nodes to a specific metric '
          'proportion; example: set weight proportion n1 n2 250km'))
    s.cust_print(self, ('set npos [node_name] [x coordinates] [y coordinates]'))
    s.cust_print(self, ('set edge weight [u] [v] [weight(pure value)]'))
    s.cust_print(self, ('remove node [node name]'))
    s.cust_print(self, ('remove edge [1st node name] [2nd node name]'))
    s.cust_print(self, ('reset plot'))
    # s.cust_print(self, ('fullscreen on/off'))
    s.cust_print(self, ('show weights on/off'))
    s.cust_print(self, (
        'drawstyle [style]. Acceptable styles are: planar/default, shell, spring, spectral, random, circular, none'))
    s.cust_print(self, ('convert [dist/metrics] [value]'))
    s.cust_print(self, ('get node dist [node1] [node2]'))
    s.cust_print(self, ('get dist [x1 coordinates] [y1 coordinates] [x2 coordinates] [y2 coordinates]'))
    s.cust_print(self, ('print nodes'))
    s.cust_print(self, ('print edges'))
    s.cust_print(self, ('print one [node_name]'))
    s.cust_print(self, ('print style : to see current drawstyle'))
    s.cust_print(self, ('help'))
    s.cust_print(self, ('floyd'))
    s.cust_print(self, ('shmoys [warehouse amount] [initial radius] [initial node name, use None for random]'))
    s.cust_print(self, ('cshmoys [warehouse amount] [initial radius] [initial node name, use None for random] [cycles]'))
    # s.cust_print(self, ('exit'))


