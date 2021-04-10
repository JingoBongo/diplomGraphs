import settings as s


def process_graph_type(graph_type):
    if 'digraph' in graph_type:
        s.graph = s.nx.DiGraph()
    else:
        s.graph = s.nx.Graph()


def add_b_edge(raw_input: str):
    # global graph
    # global successfulCommand
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
    # global graph
    # global successfulCommand
    list = raw_input.split(' ')
    if len(list) == 4:
        s.graph.add_node(list[2], weight=list[3], color='red', name=list[2])
        s.successfulCommand = True
    elif len(list) == 3:
        s.graph.add_node(list[2], color='red', name=list[2])
        s.successfulCommand = True
    else:
        print('Improper command caught in add node: ' + raw_input)


def add_edge(raw_input: str):
    # global graph
    # global successfulCommand
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
    # global successfulCommand
    # global graph
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
    else:
        print(s.graph.nodes.keys())
        print(s.graph.nodes.values())
        print('What is this option?(caught in print): ' + raw_input)


def draw_graph():
    colors = [s.graph.nodes[a].get('color', 'red') for a in s.graph.nodes]
    # please tell me why exactly colors work this way, but weights not
    # and why the way weight work colors don't want to?!
    pos = s.nx.planar_layout(s.graph)
    s.nx.draw(s.graph, pos, node_color=colors)
    labels = s.nx.get_edge_attributes(s.graph, 'weight')
    nd_labels = s.nx.get_node_attributes(s.graph, 'name')
    s.nx.draw_networkx_edge_labels(s.graph, pos, edge_labels=labels)
    s.nx.draw_networkx_labels(s.graph, pos, labels=nd_labels)
    # test feature to get fullscreen
    mng = s.plt.get_current_fig_manager()
    if mng.window.state != 'zoomed':
        mng.window.state('zoomed')


def import_json(raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        filename = list[2]
        f = open(filename)
        s.graph = s.json_graph.node_link_graph(s.json.load(f))
        f.close()
        s.successfulCommand = True
    else:
        print('Improper command caught in import json: ' + raw_input)


def import_gexf(raw_input):
    list = raw_input.split(' ')
    if len(list) == 3:
        filename = list[2]
        s.graph = s.nx.read_gexf(filename)
        s.successfulCommand = True
    else:
        print('Improper command caught in import gexf: ' + raw_input)
