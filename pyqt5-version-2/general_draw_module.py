import settings as s


def process_graph_type(graph_type):
    if 'digraph' in graph_type:
        s.graph = s.nx.DiGraph()
    else:
        s.graph = s.nx.Graph()


def add_b_edge(self, raw_input: str):
    list = raw_input.split(' ')
    if '.DiGraph' in str(type(s.graph)):
        if len(list) == 7:
            # first, add nodes with corresponding parameters
            add_node('add node ' + list[3])
            add_node('add node ' + list[4])
            s.graph.add_edge(list[3], list[4], weight=list[5])
            s.graph.add_edge(list[4], list[3], weight=list[6])
            s.successfulCommand = True
        elif len(list) == 6:
            # first, add nodes with corresponding parameters
            add_node('add node ' + list[3])
            add_node('add node ' + list[4])
            s.graph.add_edge(list[3], list[4], weight=list[5])
            s.graph.add_edge(list[4], list[3], weight=list[5])
            s.successfulCommand = True
        elif len(list) == 5:
            # first, add nodes with corresponding parameters
            add_node('add node ' + list[3])
            add_node('add node ' + list[4])
            s.graph.add_edge(list[3], list[4], weight=0)
            s.graph.add_edge(list[4], list[3], weight=0)
        else:
            s.cust_print(self, ('Improper command caught in add bidirectional edge: ' + raw_input))
    if '.Graph' in str(type(s.graph)):
        if len(list) == 6:
            # first, add nodes with corresponding parameters
            add_node('add node ' + list[3])
            add_node('add node ' + list[4])
            s.graph.add_edge(list[3], list[4], weight=list[5])
            s.successfulCommand = True
        elif len(list) == 5:
            # first, add nodes with corresponding parameters
            add_node('add node ' + list[3])
            add_node('add node ' + list[4])
            s.graph.add_edge(list[3], list[4], weight=0)
            s.successfulCommand = True
        else:
            s.cust_print(self, ('Improper command caught in add bidirectional edge: ' + raw_input))


def add_node(self, raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 4:
        s.graph.add_node(list[2], weight=list[3], color=s.default_node_color, name=list[2], pos='None')
        s.successfulCommand = True
    elif len(list) == 3:
        s.graph.add_node(list[2], color=s.default_node_color, name=list[2], pos='None')
        s.successfulCommand = True
    else:
        s.cust_print(self, ('Improper command caught in add node: ' + raw_input))


def show_edge_weights(self, raw_input: str):  # show0 weights1 on/off2
    list = raw_input.split(' ')
    if len(list) == 3:
        if list[2] == 'on':
            s.show_weight_labels = True
        else:
            s.show_weight_labels = False
    else:
        s.cust_print(self, ('Improper command caught in add node: ' + raw_input))


def swap_colors(self, raw_input: str):  # swap0 colors1 colorone2 colortwo3
    list = raw_input.split(' ')
    if len(list) == 4:
        for g in s.graph.nodes:
            if s.graph.nodes[g]['color'] == str(list[2]):
                s.graph.nodes[g]['color'] = str(list[3])
        s.successfulCommand = True
    else:
        s.cust_print(self, ('Improper command caught in swap colors: ' + raw_input))


def add_posed_node(self, raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 6:
        s.graph.add_node(list[2], weight=list[3], color=s.default_node_color, name=list[2],
                         pos=str(list[4]) + ';' + str(list[5]))
        s.successfulCommand = True
    elif len(list) == 5:
        s.graph.add_node(list[2], color=s.default_node_color, name=list[2], pos=str(list[3]) + ';' + str(list[4]))
        s.successfulCommand = True
    else:
        s.cust_print(self, ('Improper command caught in add node: ' + raw_input))


def convert(self, raw_input: str): # convert0 dist/metr1 500_2
    list = raw_input.split(' ')
    # (prop_m * edge dist) / prop_d
    if len(list) == 3:
        if 'dist' in raw_input:
            metrics = float(float(s.prop_m) * float(list[2]) / float(s.prop_d))
            s.cust_print(self, ('it corresponds to '+str(metrics)+ ' '+str(s.prop_m_suffix)))
        else:
            dist = float(float(s.prop_d) * float(list[2]) / float(s.prop_m))
            s.cust_print(self, ('it corresponds to '+str(dist)))
    else:
        s.cust_print(self, ('Improper command caught in converting values: ' + raw_input))


def set_node_pos(self, raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 5:
        try:
            s.graph.nodes[list[2]]['pos'] = str(list[3]) + ';' + str(list[4])
            s.successfulCommand = True
        except Exception as e:
            s.cust_print(self, ('Something went wrong while setting node position'))
    else:
        s.cust_print(self, ('Improper command caught in set node pos: ' + raw_input))




def set_edge_weight(self, raw_input: str):  # set0 edge1 weight2 u3 v4 weight5
    list = raw_input.split(' ')  # edge = ('n0', 'n1')  [round(float(loc_arr[0]), 4), round(float(loc_arr[1]), 4)]
    if len(list) == 6:
        try:
            s.graph[str(list[3])][str(list[4])]['weight'] = round(float(list[5]), 4)
            s.successfulCommand = True
        except Exception as e:
            s.cust_print(self, ('Something went wrong while setting edge weight'))
    else:
        s.cust_print(self, ('Improper command caught in set weight: ' + raw_input))


def get_node_dist(self, raw_input: str):
    list = raw_input.split(' ')  # get0 node1 dist3 u4 v5
    if len(list) == 5:
        try:
            pos1 = s.graph.nodes[str(list[3])]['pos']
            pos1x = float(str(pos1).split(';')[0])
            pos1y = float(str(pos1).split(';')[1])
            pos2 = s.graph.nodes[str(list[4])]['pos']
            pos2x = float(str(pos2).split(';')[0])
            pos2y = float(str(pos2).split(';')[1])
            s.distance_out_loud = True
            get_dist_between_two_points(self, pos1x, pos1y, pos2x, pos2y)
        except Exception as e:
            s.cust_print(self, ('Something went wrong while getting node positions'))
    else:
        s.cust_print(self, ('Improper command caught in get node dist: ' + raw_input))


def get_dist_between_two_points(self, x1, y1, x2, y2):
    pos1x = float(str(x1))
    pos1y = float(str(y1))
    pos2x = float(str(x2))
    pos2y = float(str(y2))
    x = pos1x - pos2x
    y = pos1y - pos2y
    dist = round(s.math.sqrt(x * x + y * y), 4)
    metrics = float(float(s.prop_m) * float(dist) / float(s.prop_d))
    if s.distance_out_loud:
        s.cust_print(self, ('Distance between 2 points: ' + str(dist)+'; or '+str(metrics)+' '+str(s.prop_m_suffix)))
        s.distance_out_loud = False
    return dist


def set_weight_proportion(self, raw_input: str):  # set0 weight1 proportion2 u3 v4 xxxKm5
    list = raw_input.split(' ')  # edge = ('n0', 'n1')
    if len(list) == 6:
        try:
            # w = s.graph[str(list[3])][str(list[4])]['weight']
            pos1 = s.graph.nodes[str(list[3])]['pos']
            pos1x = float(str(pos1).split(';')[0])
            pos1y = float(str(pos1).split(';')[1])
            pos2 = s.graph.nodes[str(list[4])]['pos']
            pos2x = float(str(pos2).split(';')[0])
            pos2y = float(str(pos2).split(';')[1])
            dist = get_dist_between_two_points(self, pos1x, pos1y, pos2x, pos2y)
            s.prop_d = float(dist)
            # s.prop_m = ''.join(re.findall(r"[-+]?\d*\.\d+|\d+", str(list[5])))
            if str(list[5])[-2].isdigit():
                s.prop_m = str(list[5][:-1])
                s.prop_m_suffix = str(list[5][-1])
            else:
                s.prop_m = str(list[5][:-2])
                s.prop_m_suffix = str(list[5][-2]) + str(list[5][-1])
            s.cust_print(self, ('new distance proportion: ' + str(s.prop_d) + ' = ' + str(s.prop_m) + ' ' + str(s.prop_m_suffix)))
        except Exception as e:
            s.cust_print(self, ('Something went wrong while setting weight proportion'))
    else:
        s.cust_print(self, ('Improper command caught in set weight proportion: ' + raw_input))


def add_edge(self, raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 5:
        if list[2] in s.graph.nodes and list[3] in s.graph.nodes:
            s.graph.add_edge(list[2], list[3], weight=round(float(list[4]), 4))  # list[4]
            s.successfulCommand = True
        else:
            s.cust_print(self, ('abort adding edge, one of nodes is missing. (hint: command print nodes)'))
    elif len(list) == 4:
        if list[2] in s.graph.nodes and list[3] in s.graph.nodes:
            s.graph.add_edge(list[2], list[3], weight=0)
            s.successfulCommand = True
        else:
            s.cust_print(self, ('abort adding edge, one of nodes is missing. (hint: command print nodes)'))
    else:
        s.cust_print(self, ('Improper command caught in add edge: ' + raw_input))



def remove_edge(self, raw_input: str):  # remove0 edge1 u2 v3
    #    remove node x1
    list = raw_input.split(' ')
    if len(list) == 4:
        try:
            s.graph.remove_edge(str(list[2]), str(list[3]))
            s.successfulCommand = True
        except Exception as e:
            s.cust_print(self, (e))
            s.cust_print(self, ('Failed to remove edge'))
    else:
        s.cust_print(self, ('Improper command caught in remove edge: ' + raw_input))


def fullscreen(self, raw_input: str):
    #    remove edge x1 x2
    list = raw_input.split(' ')
    if len(list) == 2:
        if 'on' == list[1]:
            s.fullscreen = True
        elif 'off' == list[1]:
            s.fullscreen = False
        else:
            s.cust_print(self, ('Improper command caught in fullscreen: ' + raw_input))
    else:
        s.cust_print(self, ('Improper command caught in fullscreen: ' + raw_input))


def remove_node(self, raw_input: str):
    #    remove node x1
    list = raw_input.split(' ')
    if len(list) == 3:
        try:
            s.graph.remove_node(list[2])
            s.successfulCommand = True
        except Exception as e:
            s.cust_print(self, ('something went wrong when removing node, make sure it exists'))
    else:
        s.cust_print(self, ('Improper command caught in remove node: ' + raw_input))


def reset_plot():
    s.successfulCommand = True
    # g_type = input('Please specify graph type(graph/digraph): >>')
    # process_graph_type(g_type)
    s.graph.clear()


def save_image(self, raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        s.filename = list[2]
        s.successfulCommand = True
        now = s.datetime.datetime.now()
        file_name = s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.png'
        file_plus_path = str(s.getcwd()) + '\\' + file_name
        s.plt.savefig(file_plus_path)
        s.cust_print(self, (str(file_plus_path) + ' was saved.'))

    else:
        s.cust_print(self, ('Improper command caught in save image: ' + raw_input))



def save_json(self, raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        s.filename = list[2]
        s.successfulCommand = True
        now = s.datetime.datetime.now()
        file_name = s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.json'
        file_plus_path = str(s.getcwd()) + '\\' + file_name
        f = open(file_plus_path, 'a')
        f.write(s.json.dumps(s.json_graph.node_link_data(s.graph)))
        f.close()
        s.cust_print(self, (str(file_plus_path) + ' was saved.'))
    else:
        s.cust_print(self, ('Improper command caught in save json: ' + raw_input))


def save_gexf(self, raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        s.filename = list[2]
        s.successfulCommand = True
        now = s.datetime.datetime.now()
        file_name = s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.gexf'
        file_plus_path = str(s.getcwd()) + '\\' + file_name
        s.nx.write_gexf(s.graph, file_plus_path)
        s.cust_print(self, (str(file_plus_path) + ' was saved.'))
    else:
        s.cust_print(self, ('Improper command caught in save gexf: ' + raw_input))


def print_list(self, raw_input):
    if 'edges' in raw_input:
        s.cust_print(self, (s.graph.edges))
        for e in s.graph.edges:
            s.cust_print(self, (str(e) + ' : ' + str(s.graph.edges[e]['weight'])))
        #
        # labels = s.nx.get_edge_attributes(s.graph, 'weight')
        # s.cust_print(self, labels)
        # colors = [s.graph.nodes[a].get('weight', 0) for a in s.graph.nodes]
        # s.cust_print(self, colors)
    elif 'nodes' in raw_input:
        s.cust_print(self, (s.graph.nodes))
    elif 'style' in raw_input:
        s.cust_print(self, ('current drawstyle is: ' + str(s.draw_style)))
    elif 'one' in raw_input:
        try:
            s.cust_print(self, (s.graph.nodes[str(raw_input).split(' ')[-1]]))
        except Exception as e:
            s.cust_print(self, ('Failed to print info about node: ' + str(raw_input)))
    else:
        s.cust_print(self, (s.graph.nodes.keys()))
        s.cust_print(self, (s.graph.nodes.values()))
        s.cust_print(self, ('What is this option?(caught in print): ' + raw_input))


def define_draw_style(self, raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        if list[1] == 'none':
            s.cust_print(self, ('Selected none drawstyle. Make sure to set up all node positions!'))
        s.draw_style = list[1]
        s.successfulCommand = True
    else:
        s.cust_print(self, ('Improper command caught in drawstyle: ' + raw_input))


def draw_graph(self):
    self.figure.clf()
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
        pos = generate_custom_pos(self)
    elif s.draw_style == 'random':
        pos = s.nx.random_layout(s.graph)
    elif s.draw_style == 'circular':
        pos = s.nx.circular_layout(s.graph)
    else:
        s.cust_print(self,
                     ('Hard switch to planar. What is this draw style? ' + s.draw_style + '; Please define a valid one (see help).'))
        pos = s.nx.planar_layout(s.graph)

    if s.background_is_image:
        implot = s.plt.imshow(s.background_img)

    s.nx.draw(s.graph, pos, node_color=colors)
    labels = s.nx.get_edge_attributes(s.graph, 'weight')
    nd_labels = s.nx.get_node_attributes(s.graph, 'name')
    if s.show_weight_labels:
        s.nx.draw_networkx_edge_labels(s.graph, pos, edge_labels=labels)
    s.nx.draw_networkx_labels(s.graph, pos, labels=nd_labels)

    self.canvas.draw_idle()
    # s.cust_print('graph ready')


def generate_custom_pos(self):
    emptyDict = {}
    # s.cust_print(self, 'custom pos generation started')
    for n in s.graph.nodes:
        try:
            if s.graph.nodes[n]['pos'] == 'None' or s.graph.nodes[n]['pos'] is None:
                s.cust_print(self, (str(n) + ' _node has no pos, set it up properly'))
                s.cust_print(self, (str(n) + ' has invalid position, using default layout'))
                s.draw_style = 'default'
                emptyDict = s.nx.planar_layout(s.graph)
                return emptyDict
            else:
                loc_arr = str(s.graph.nodes[n]['pos']).split(';')
                emptyDict[n] = [round(float(loc_arr[0]), 4), round(float(loc_arr[1]), 4)]
        except Exception as e:
            s.cust_print(self, (str(n) + ' has invalid position, using default layout(exception)'))
            s.draw_style = 'default'
            emptyDict = s.nx.planar_layout(s.graph)
            return emptyDict
    # s.cust_print(self, 'result of custom generation:')
    # s.cust_print(self, emptyDict)
    return emptyDict


def find_next_generica_node_name_counter():
    var = 0
    for n in s.graph.nodes:
        ncounter  = int(s.re.sub('[^0-9]', "", str(n)))
        if ncounter > var:
            var = ncounter
    return var + 1


def import_json(self, raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        filename = list[1]
        try:
            f = open(filename)
            s.graph = s.json_graph.node_link_graph(s.json.load(f))
            f.close()
            s.generic_node_name_counter = find_next_generica_node_name_counter()
            s.successfulCommand = True
        except Exception as e:
            s.cust_print(self, ('something went wrong while importing file '+str(filename)))
            s.cust_print(self, e)
    else:
        s.cust_print(self, ('Improper command caught in import json: ' + raw_input))


def import_png(self, raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        try:
            s.background_img = s.plt.imread(raw_input.split(' ')[1])
            s.successfulCommand = True
            s.background_is_image = True
        except Exception as e:
            s.cust_print(self, ('something went wrong while importing file '+str(raw_input.split(' ')[1])))
            s.cust_print(self, (e))
    else:
        s.cust_print(self, ('Improper command caught in import png: ' + raw_input))


def import_gexf(self, raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        filename = list[1]
        try:
            s.graph = s.nx.read_gexf(filename)
            s.generic_node_name_counter = find_next_generica_node_name_counter()
            s.successfulCommand = True
        except Exception as e:
            s.cust_print(self, ('something went wrong while importing file '+str(filename)))
            s.cust_print(self, (e))
    else:
        s.cust_print(self, ('Improper command caught in import gexf: ' + raw_input))


def change_node_color(self, raw_input):  # change0 node1 color2 [nodename]3 [color]4
    list = raw_input.split(' ')
    if len(list) == 5:
        try:
            s.graph.nodes[list[3]]['color'] = list[4]
            s.successfulCommand = True
        except Exception as e:
            s.cust_print(self, ('Something went wrong while assigning node color, please make sure such node or color exists'))
    else:
        s.cust_print(self, ('Improper command caught in change node color: ' + raw_input))



def set_mouse_listener(self):
    self.canvas.mpl_connect('button_release_event', lambda event: on_click(self, event))
    # self_fig.canvas.mpl_connect('key_release_event', release)


# def release(event):
#     # s.cust_print(self, 'press', event.key)
#     # if event.key == 'x':
#     #     s.cust_print(self, 'it was the X spot')
#     pass


def on_click(self, event):
    if event.dblclick:
        pass
    if event.button:
        if event.button == 3:
            round(float(event.xdata), 4)
            add_posed_node(self, 'add pnode ' + s.generic_node_name + str(s.generic_node_name_counter) + ' ' + str(round(float(event.xdata), 4)) + ' ' + str(round(float(event.ydata), 4)))
            s.generic_node_name_counter += 1
            draw_graph(self)
        if event.button == 2:
            try:
                for n in s.graph.nodes:
                    npos = s.graph.nodes[n]['pos']
                    nx = float(str(npos).split(';')[0])
                    ny = float(str(npos).split(';')[1])
                    if get_dist_between_two_points(self, round(float(event.xdata), 4), round(float(event.ydata), 4), nx, ny) <= 15:
                        s.mouse_clicked_nodes.append(n)
                        break
                if len(s.mouse_clicked_nodes) >= 2:
                    n1x = str(s.graph.nodes[str(s.mouse_clicked_nodes[0])]['pos']).split(';')[0]
                    n1y = str(s.graph.nodes[str(s.mouse_clicked_nodes[0])]['pos']).split(';')[1]
                    n2x = str(s.graph.nodes[str(s.mouse_clicked_nodes[1])]['pos']).split(';')[0]
                    n2y = str(s.graph.nodes[str(s.mouse_clicked_nodes[1])]['pos']).split(';')[1]
                    dist = get_dist_between_two_points(self, n1x, n1y, n2x, n2y)
                    weight = float((float(s.prop_m) * float(dist)) / float(s.prop_d))
                    add_edge(self, 'add edge '+str(s.mouse_clicked_nodes[0]) + ' ' + str(s.mouse_clicked_nodes[1]) + ' ' + str(weight))
                    s.mouse_clicked_nodes.clear()
                    draw_graph(self)
            except Exception as e:
                s.cust_print(self, ('something went wrong while creating edge with mouse'))
                s.cust_print(self, (e))
        if event.button == 1:
            if event.xdata:
                s.cust_print(self, ('mouse pos: ' + str(round(float(event.xdata), 4)) + ' ' + str(round(float(event.xdata), 4))))


