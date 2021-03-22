import networkx as nx
import matplotlib.pyplot as plt
import pathlib

whileBool = True
successfulCommand = False
requires_saving = False
graph = nx.Graph()
figure = None
filename = None


def add_node(raw_input: str):
    global graph
    global successfulCommand
    list = raw_input.split(' ')
    if len(list) == 4:
        graph.add_node(list[2], weight=list[3])
        successfulCommand = True
    elif len(list) == 3:
        graph.add_node(list[2])
        successfulCommand = True
    else:
        print('Improper command caught in add node: ' + raw_input)


def add_edge(raw_input: str):
    global graph
    global successfulCommand
    list = raw_input.split(' ')
    if len(list) == 5:
        graph.add_edge(list[2], list[3], weight=list[4])
        successfulCommand = True
    elif len(list) == 4:
        graph.add_edge(list[2], list[3])
        successfulCommand = True
    else:
        print('Improper command caught in add edge: ' + raw_input)


def reset_plot():
    global successfulCommand
    global graph
    successfulCommand = True
    gType = input('Please specify graph type(graph/digraph): >>')
    process_graph_type(gType)
    graph.clear()


def help():
    print('commands are:')
    print('add node [node_name] (possible node weight)')
    print('add edge [1st node name] [2nd node name] (possible edge weight)')
    if '.DiGraph' in str(type(graph)):
        print('add bidirectional edge [1st node name] [2nd node name] (possible edge weight)')
    print('reset plot')
    print('help')
    print('save image [image name]')
    print('exit')


def save_image(raw_input):
    global successfulCommand
    global figure
    global requires_saving
    list = raw_input.split(' ')
    global filename
    if len(list) == 3:
        filename = list[2]
        # figure.savefig(str(pathlib.Path(__file__).parent.parent.absolute()) + '/images/' + list[2] + ".png")
        successfulCommand = True
        requires_saving = True
    else:
        print('Improper command caught in save image: ' + raw_input)


def print_list(raw_input):
    if 'edges' in raw_input:
        print(graph.edges)
    elif 'nodes' in raw_input:
        print(graph.nodes)
    else:
        print('What is this option?(caught in print): ' + raw_input)


def add_b_edge(raw_input: str):
    global graph
    global successfulCommand
    list = raw_input.split(' ')
    if '.DiGraph' in str(type(graph)):
        if len(list) == 7:
            graph.add_edge(list[3], list[4], weight=list[5])
            graph.add_edge(list[4], list[3], weight=list[6])
            successfulCommand = True
        elif len(list) == 6:
            graph.add_edge(list[3], list[4], weight=list[5])
            graph.add_edge(list[4], list[3], weight=list[5])
            successfulCommand = True
        elif len(list) == 5:
            graph.add_edge(list[3], list[4])
            graph.add_edge(list[4], list[3])
        else:
            print('Improper command caught in add bidirectional edge: ' + raw_input)
    if '.Graph' in str(type(graph)):
        if len(list) == 6:
            graph.add_edge(list[3], list[4], weight=list[5])
            successfulCommand = True
        elif len(list) == 5:
            graph.add_edge(list[3], list[4])
            successfulCommand = True
        else:
            print('Improper command caught in add bidirectional edge: ' + raw_input)


def process_raw_input(raw_input: str):
    global whileBool
    if 'help' in raw_input:
        help()
    elif 'add node' in raw_input:
        add_node(raw_input)
    elif 'add edge' in raw_input:
        add_edge(raw_input)
    elif 'add bidirectional edge' in raw_input:
        add_b_edge(raw_input)
    elif 'reset plot' in raw_input:
        reset_plot()
    elif 'save image' in raw_input:
        save_image(raw_input)
    elif 'print' in raw_input:
        print_list(raw_input)
    elif 'exit' in raw_input:
        whileBool = False
        print('Closing everything')
        plt.close()
    else:
        print('Command not recognized: ' + raw_input)


def process_graph_type(graphType):
    global graph
    if 'digraph' in graphType:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()


graphType = input('Please specify graph type(graph/digraph): >>')
process_graph_type(graphType)
while whileBool:
    print('Enter command. \'help\' for help')
    raw_input = input('>>')
    process_raw_input(raw_input)
    if successfulCommand:
        successfulCommand = False
        nx.draw_circular(graph,
                         node_color='red',
                         node_size=1000,
                         with_labels=True)
        plt.ion()
        plt.pause(0.001)
        if requires_saving:
            requires_saving = False
            plt.savefig(str(pathlib.Path(__file__).parent.parent.absolute()) + '/images/'+filename+'.png')
        plt.show()
        plt.clf()
