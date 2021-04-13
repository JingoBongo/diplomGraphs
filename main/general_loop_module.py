import settings as s
import general_draw_module as dm
import general_alg_module as am


def process_raw_input(raw_input: str):
    if 'help' in raw_input:
        help()
    elif 'add node' in raw_input:
        dm.add_node(raw_input)
    elif 'show weights' in raw_input:
        dm.show_edge_weights(raw_input)
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
    elif 'set weight proportion' in raw_input:
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
    # elif 'play' in raw_input:
    #     # s.plt.ion()
    #     s.plt.show(block=False)
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
    elif 'keepalive' in raw_input:
        s.plt.show()
        s.plt.ion()
        s.plt.pause(0.001)
    elif 'import' in raw_input:
        if '.json' in raw_input:
            dm.import_json(raw_input)
        elif '.gexf' in raw_input:
            dm.import_gexf(raw_input)
        elif '.png' in raw_input:
            dm.import_png(raw_input)
        else:
            print('What is the file format from command? I accept .png, .gexf and .json: ' + str(raw_input))
    elif 'change node color' in raw_input:
        dm.change_node_color(raw_input)
    # elif 'enable plot' in raw_input or 'disable plot' in raw_input:
    #     dm.plot_enabler(raw_input)
    elif 'print' in raw_input:
        dm.print_list(raw_input)
    elif 'floyd' in raw_input:
        am.dum_dum_floyd_alg()
    elif 'shmoys' in raw_input:
        if len(raw_input.split(' ')) == 4:   # shmoys wh rad startingNode
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


def help():
    print('commands are:')
    print('add node [node_name] (possible node weight)')
    print('add edge [1st node name] [2nd node name] (possible edge weight)')
    print('change node color [node name] [color]')
    print('remove node [node name]')
    print('remove edge [1st node name] [2nd node name]')
    if '.DiGraph' in str(type(s.graph)):
        print('add bidirectional edge [1st node name] [2nd node name] (possible edge weight)')
    print('reset plot')
    print('help')
    print('print [type] ; Type could be nodes or edges')
    print('save image [image name]')
    print('save json [file name]')
    print('save gexf [file name]')
    print('import [path(if not from .py file folder) + filename] ; I accept .gexf and .json')
    print('floyd')
    print('shmoys [warehouse amount] [initial radius] [initial node name, use None for random]')
    print(
        'drawstyle [style]. Acceptable styles are: planar/default, shell, spring, spectral, random, circular')  # kamada_kawai, out temporarily
    print('exit')


def main_loop():
    # dm.init_plot()
    dm.gui()
    # I dont use DiGraphs now, so I cut it temporarily. I will still live this as a commands option
    # graph_type = input('Please specify graph type(graph/digraph): >>')
    # dm.process_graph_type(graph_type)
    dm.process_graph_type('g')
    while s.whileBool:
        print('Enter command. \'help\' for help')
        raw_input = input('>>')
        process_raw_input(raw_input)
        if s.successfulCommand:
            s.successfulCommand = False
            # s.plt.clf()
            dm.draw_graph()
            s.plt.show()
            s.plt.ion()
            s.plt.pause(0.001)
            if s.requires_saving:
                s.requires_saving = False
                now = s.datetime.datetime.now()
                file_name = s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.png'
                file_plus_path = str(s.pathlib.Path(__file__).parent.parent.absolute()) + '\\images\\' + file_name
                s.plt.savefig(file_plus_path)
                print(str(file_name) + ' was saved.')
            if s.requires_saving_json:
                s.requires_saving_json = False
                now = s.datetime.datetime.now()
                file_name = s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.json'
                file_plus_path = str(s.pathlib.Path(__file__).parent.parent.absolute()) + '\\saved_graphs\\' + file_name
                f = open(file_plus_path, 'a')
                f.write(s.json.dumps(s.json_graph.node_link_data(s.graph)))
                f.close()
                print(str(file_name) + ' was saved.')
            if s.requires_saving_gexf:
                s.requires_saving_gexf = False
                now = s.datetime.datetime.now()
                file_name = s.filename + now.strftime("-%m-%d-%Y--%H-%M-%S") + '.gexf'
                file_plus_path = str(s.pathlib.Path(__file__).parent.parent.absolute()) + '\\saved_graphs\\' + file_name
                s.nx.write_gexf(s.graph, file_plus_path)
                print(str(file_name) + ' was saved.')
            # add bool to check for show or not
            # print(s.draw_plot)
            # if s.draw_plot:
            #     s.plt.ion()
            #     s.plt.show()
            # else:
            #     s.plt.ioff()
            # this part is in maintenance

        # another portion of junk code I will not need for a while
        # elif 'init1' in raw_input:
        #     method_to_call = getattr(am, str(raw_input.split(' ')[1]))
        #     result = method_to_call(raw_input.split(' ')[2])
        # elif 'init2' in raw_input:
        #     method_to_call = getattr(am, str(raw_input.split(' ')[1]))
        #     result = method_to_call(raw_input.split(' ')[2], raw_input.split(' ')[3])
        # elif 'init3' in raw_input:
        #     method_to_call = getattr(am, str(raw_input.split(' ')[1]))
        #     result = method_to_call(raw_input.split(' ')[2], raw_input.split(' ')[3], raw_input.split(' ')[4])
