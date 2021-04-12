import settings as s



def process_graph_type(graph_type):
    if 'digraph' in graph_type:
        s.graph = s.nx.DiGraph()
    else:
        s.graph = s.nx.Graph()


def add_b_edge(raw_input: str):
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
            print('Improper command caught in add bidirectional edge: ' + raw_input)
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
            print('Improper command caught in add bidirectional edge: ' + raw_input)


def add_node(raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 4:
        s.graph.add_node(list[2], weight=list[3], color=s.default_node_color, name=list[2], pos = 'None')
        s.successfulCommand = True
    elif len(list) == 3:
        s.graph.add_node(list[2], color=s.default_node_color, name=list[2], pos = 'None')
        s.successfulCommand = True
    else:
        print('Improper command caught in add node: ' + raw_input)

def add_posed_node(raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 6:
        s.graph.add_node(list[2], weight=list[3], color=s.default_node_color, name=list[2], pos = str(list[4])+';'+str(list[5]))
        s.successfulCommand = True
    elif len(list) == 5:
        s.graph.add_node(list[2], color=s.default_node_color, name=list[2], pos = str(list[3])+';'+str(list[4]))
        s.successfulCommand = True
    else:
        print('Improper command caught in add node: ' + raw_input)


def set_node_pos(raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 5:
        try:
            s.graph.nodes[list[2]]['pos'] = str(list[3])+';'+str(list[4])
            s.successfulCommand = True
        except Exception as e:
            print('Something went wrong while setting node position')
    else:
        print('Improper command caught in set node pos: ' + raw_input)

def add_edge(raw_input: str):
    list = raw_input.split(' ')
    if len(list) == 5:
        # first, add nodes with corresponding parameters
        add_node('add node ' + list[2])
        add_node('add node ' + list[3])
        s.graph.add_edge(list[2], list[3], weight=list[4])
        s.successfulCommand = True
    elif len(list) == 4:
        # first, add nodes with corresponding parameters
        add_node('add node ' + list[2])
        add_node('add node ' + list[3])
        s.graph.add_edge(list[2], list[3], weight=0)
        s.successfulCommand = True
    else:
        print('Improper command caught in add edge: ' + raw_input)


def remove_edge(raw_input: str):
    #    remove edge x1 x2
    list = raw_input.split(' ')
    if len(list) == 4:
        s.graph.remove_edge(list[2], list[3])
        s.successfulCommand = True
    else:
        print('Improper command caught in remove edge: ' + raw_input)


def remove_node(raw_input: str):
    #    remove node x1
    list = raw_input.split(' ')
    if len(list) == 3:
        s.graph.remove_node(list[2])
        s.successfulCommand = True
    else:
        print('Improper command caught in remove node: ' + raw_input)


def reset_plot():
    s.successfulCommand = True
    g_type = input('Please specify graph type(graph/digraph): >>')
    process_graph_type(g_type)
    s.graph.clear()


def save_image(raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        s.filename = list[2]
        s.successfulCommand = True
        s.requires_saving = True
    else:
        print('Improper command caught in save image: ' + raw_input)


def save_json(raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        s.filename = list[2]
        s.successfulCommand = True
        s.requires_saving_json = True
    else:
        print('Improper command caught in save json: ' + raw_input)


def save_gexf(raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        s.filename = list[2]
        s.successfulCommand = True
        s.requires_saving_gexf = True
    else:
        print('Improper command caught in save gexf: ' + raw_input)


def print_list(raw_input):
    if 'edges' in raw_input:
        print(s.graph.edges)
        print(s.graph.get_edge_data('weight'))
        #
        # labels = s.nx.get_edge_attributes(s.graph, 'weight')
        # print(labels)
        # colors = [s.graph.nodes[a].get('weight', 0) for a in s.graph.nodes]
        # print(colors)
    elif 'nodes' in raw_input:
        print(s.graph.nodes)
    elif 'one' in raw_input:
        try:
            print(s.graph.nodes[str(raw_input).split(' ')[-1]])
        except Exception as e:
            print('Failed to print info about node: '+str(raw_input))
    else:
        print(s.graph.nodes.keys())
        print(s.graph.nodes.values())
        print('What is this option?(caught in print): ' + raw_input)


def define_draw_style(raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        s.draw_style = list[1]
        s.successfulCommand = True
    else:
        print('Improper command caught in drawstyle: ' + raw_input)


def draw_graph():
    # init_plot()
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
        print('Make sure to set up all node positions!')
    elif s.draw_style == 'random':
        pos = s.nx.random_layout(s.graph)
    # elif s.draw_style == 'kamada_kawai': # doesnt work right now, it needs distances (ex.: https://github.com/RasaHQ/whatlies/issues/9)
    #     pos = s.nx.kamada_kawai_layout(s.graph)
    elif s.draw_style == 'circular':
        pos = s.nx.circular_layout(s.graph)
    else:
        print(
            'Hard switch to planar. What is this draw style? ' + s.draw_style + '; Please define a valid one (see help).')
        pos = s.nx.planar_layout(s.graph)


    # for n in s.graph.nodes:
    #     try:
    #         if s.graph.nodes[n]['pos'] == 'None':
    #             s.graph.nodes[n]['pos'] = pos.get(n)
    #     except KeyError as e:
    #         s.graph.nodes[n]['pos'] = pos.get(n)


    print('position from generated pos')
    print(pos)
    for n in s.graph.nodes:
        print(str(s.graph.nodes[n]['pos']))
    print(pos)
    implot = s.plt.imshow(s.background_img)
    s.nx.draw(s.graph, pos, node_color=colors)
    labels = s.nx.get_edge_attributes(s.graph, 'weight')
    nd_labels = s.nx.get_node_attributes(s.graph, 'name')
    s.nx.draw_networkx_edge_labels(s.graph, pos, edge_labels=labels)
    s.nx.draw_networkx_labels(s.graph, pos, labels=nd_labels)
    # test feature to get fullscreen
    # mng = s.plt.get_current_fig_manager()
    # if mng.window.state != 'zoomed':
    #     mng.window.state('zoomed')


def generate_custom_pos():
    emptyDict = {}
    print('custom generation started')
    for n in s.graph.nodes:
        try:
            if s.graph.nodes[n]['pos'] == 'None':
                print(str(n)+ ' _node has no pos, set it up properly')
                print(str(n) + ' has invalid position, using default layout')
                s.draw_style = 'default'
                emptyDict = s.nx.planar_layout(s.graph)
            else:
                loc_arr = str(s.graph.nodes[n]['pos']).split(';')
                emptyDict[n] = (loc_arr[0], loc_arr[1])
        except Exception as e:
            print(str(n) + ' has invalid position, using default layout')
            s.draw_style = 'default'
            emptyDict = s.nx.planar_layout(s.graph)
    print('result of custom generation:')
    print(emptyDict)
    return emptyDict


def import_json(raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        filename = list[1]
        f = open(filename)
        s.graph = s.json_graph.node_link_graph(s.json.load(f))
        f.close()
        s.successfulCommand = True
    else:
        print('Improper command caught in import json: ' + raw_input)


def import_png(raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        s.background_img = s.plt.imread(raw_input.split(' ')[1])
        s.successfulCommand = True
    else:
        print('Improper command caught in import json: ' + raw_input)


def import_gexf(raw_input):
    list = raw_input.split(' ')
    if len(list) == 2:
        filename = list[1]
        s.graph = s.nx.read_gexf(filename)
        s.successfulCommand = True
    else:
        print('Improper command caught in import gexf: ' + raw_input)


def change_node_color(raw_input):  # change0 node1 color2 [nodename]3 [color]4
    list = raw_input.split(' ')
    if len(list) == 5:
        try:
            s.graph.nodes[list[3]]['color'] = list[4]
            s.successfulCommand = True
        except Exception as e:
            print('Something went wrong while assigning node color, please make sure such node or color exists')
    else:
        print('Improper command caught in change node color: ' + raw_input)


# this part stands for making plot interactive, showing and pausing on demand
def init_plot():
    print('thats life')


def gui():
    # plt.axis([0, 10, 1, 15])
    s.plt.axis([0, 100, 0, 100])
    # ax = s.plt.subplot(111)
    fig = s.plt.gcf()
    # fig.add_axes((left, bottom, ))
    # ax = fig.add_subplot(111)
    # fig.subplots_adjust(bottom=0.2)
    # bpause = s.Button(ax, 'Pause')
    # bpause.on_clicked(on_click)
    fig.canvas.mpl_connect('button_press_event', on_click)
    fig.canvas.mpl_connect('key_release_event', release)


def release(event):
    print('press', event.key)
    if event.key == 'x':
        print('it was the X spot')


def on_click(event):
    if event.dblclick:
        print('doubleclick, doing ion + pause ')
        # s.plt.ion()
        # s.plt.pause(0.01)
    if event.button:
        # print('click actually worked '+ str(event.xdata)+' '+str(event.ydata))
        # print('button clicked: '+str(event.button))
        if event.button == 3:
            add_posed_node('add pnode '+s.generic_node_name+str(s.generic_node_name_counter)+' '+str(event.xdata)+' '+str(event.ydata))
            s.generic_node_name_counter += 1
            draw_graph()
            s.plt.show()
        if event.button == 2:
            print('inside middle')
            # s.plt.show()
            # s.plt.ion()
            # s.plt.pause(0.001)
        if event.button == 1:
            print('mouse pos: '+ str(event.xdata)+' '+str(event.ydata))

# def plot_enabler(raw_input):  # disable plot / enable plot
#     list = raw_input.split(' ')
#     if len(list) == 2:
#         if 'disable plot' == raw_input:
#             s.draw_plot = False
#             s.successfulCommand = True
#         elif 'enable plot' == raw_input:
#             s.draw_plot = True
#             s.successfulCommand = True
#         else:
#             print('Improper command caught in enable/disable plot: ' + raw_input)
#     else:
#         print('Improper command caught in enable/disable plot: ' + raw_input)
# idk why it doesnt work now. maybe because of pause, but i cant deal with it other way
