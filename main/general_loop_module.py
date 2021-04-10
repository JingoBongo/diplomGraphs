import settings as s
import general_draw_module as dm
import general_alg_module as am





def process_raw_input(raw_input: str):
    if 'help' in raw_input:
        help()
    elif 'add node' in raw_input:
        dm.add_node(raw_input)
    elif 'add edge' in raw_input:
        dm.add_edge(raw_input)
    elif 'remove node' in raw_input:
        dm.remove_node(raw_input)
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
    elif 'import json' in raw_input:
        dm.import_json(raw_input)
    elif 'import gexf' in raw_input:
        dm.import_gexf(raw_input)
    elif 'print' in raw_input:
        dm.print_list(raw_input)
    elif 'floyd' in raw_input:
        am.dum_dum_floyd_alg(s.graph)
    elif 'exit' in raw_input:
        s.whileBool = False
        print('Closing everything')
        s.plt.close()
    else:
        print('Command not recognized: ' + raw_input)

def help():
    print('commands are:')
    print('add node [node_name] (possible node weight)')
    print('add edge [1st node name] [2nd node name] (possible edge weight)')
    print('remove node [node name]')
    print('remove edge [1st node name] [2nd node name]')
    if '.DiGraph' in str(type(s.graph)):
        print('add bidirectional edge [1st node name] [2nd node name] (possible edge weight)')
    print('reset plot')
    print('help')
    print('save image [image name]')
    print('exit')


def main_loop():
    graph_type = input('Please specify graph type(graph/digraph): >>')
    dm.process_graph_type(graph_type)
    while s.whileBool:
        print('Enter command. \'help\' for help')
        raw_input = input('>>')
        process_raw_input(raw_input)
        if s.successfulCommand:
            s.successfulCommand = False

            # // replace with proper draw command
            # s.nx.draw_circular(s.graph,
            #                  node_color='red',
            #                  node_size=1000,
            #                  with_labels=True)

            dm.draw_graph()


            # labels = nx.get_edge_attributes(graph, 'weight')
            # nx.draw_networkx_edge_labels(graph, edge_labels=labels)
            s.plt.ion()
            s.plt.pause(0.001)
            if s.requires_saving:
                s.requires_saving = False
                now = s.datetime.datetime.now()
                file_plus_path = str(s.pathlib.Path(__file__).parent.parent.absolute()) + '\\images\\' + s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.png'
                s.plt.savefig(file_plus_path)
            if s.requires_saving_json:
                s.requires_saving_json = False
                now = s.datetime.datetime.now()
                file_plus_path = str(s.pathlib.Path(__file__).parent.parent.absolute()) + '\\saved_graphs\\' + s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.json'
                f = open(file_plus_path, 'a')
                f.write(s.json.dumps(s.json_graph.node_link_data(s.graph)))
                f.close()
            if s.requires_saving_gexf:
                s.requires_saving_gexf = False
                now = s.datetime.datetime.now()
                file_plus_path = str(s.pathlib.Path(__file__).parent.parent.absolute()) + '\\saved_graphs\\' + s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.gexf'
                s.nx.write_gexf(s.graph, file_plus_path)
            # add bool to check for show or not
            s.plt.show()
            s.plt.clf()