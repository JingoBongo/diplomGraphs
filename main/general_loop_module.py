import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import datetime

whileBool = True
successfulCommand = False
requires_saving = False
graph = nx.Graph()
# figure = None
# filename = ''

def process_graph_type(graphType):
    global graph
    if 'digraph' in graphType:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

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

def main_loop():
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
            # labels = nx.get_edge_attributes(graph, 'weight')
            # nx.draw_networkx_edge_labels(graph, edge_labels=labels)
            plt.ion()
            plt.pause(0.001)
            if requires_saving:
                requires_saving = False
                now = datetime.datetime.now()
                plt.savefig(str(pathlib.Path(__file__).parent.parent.absolute()) + '/images/' + filename + now.strftime(
                    "-%m/%d/%Y-%H:%M:%S-") + '.png')
            plt.show()
            plt.clf()