import networkx as nx
import matplotlib.pyplot as plt

uber_dict = {'y': {('VD3', 'VD5'): 0, ('VD3', 'VD8'): 0}, 'blue': {('R1', 'R3'): 1, ('R1', 'R2'): 1, ('R1', 'R4'): 1},
             'green': {('VD1', 'VD2'): 0, ('VD1', 'VD7'): 0, ('VD1', 'VD6'): 0},
             'red': {('DD2', 'DD3'): 4, ('DD2', 'VD4'): 1, ('DD2', 'DD1'): 5}}

g = nx.Graph()
for cvet, slovar in uber_dict.items():
    for e, p in slovar.items():
        g.add_edge(*e, p)

    pos = nx.circular_layout(g)
    edge_labels = {(u, v): d['weight'] for u, v, d in g.edges(True)}
    nx.draw_networkx_nodes(g, pos, 600, cvet)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels, 'r')

    plt.title("Входная схема")
    plt.axis('off')
    plt.show()
    # plt.savefig('output.png')