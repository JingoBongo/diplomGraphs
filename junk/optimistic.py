import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt


def add_edge(f_item, s_item, ggraph=None):
    ggraph.add_edge(f_item, s_item)
    ggraph.add_edge(s_item, f_item)


graph = nx.Graph()

# graph.add_node('A')
# graph.add_node('B')
# graph.add_node('C')

# print('cur nodes: ')
# print(graph.nodes)

# add_edge('A', 'B', ggraph=graph)
# add_edge('B', 'C', ggraph=graph)
# add_edge('B', 'D', ggraph=graph)
# add_edge('D', 'E', ggraph=graph)
# if we add edges with node names, we can ignore adding these nodes


# graph.add_edge('E', 'A')

# print('after adding edges, nodes: ')
# print(graph.nodes())


cities = {'A': (0, 20),
          'B': (15, 24),
          'C': (16, 41),
          'D': (10, 40)}

# graph = nx.Graph()  already defined that...
graph.add_nodes_from (cities)



kilometres = {('A', 'B', 15),
              ('B', 'C', 16),
              ('B', 'D', 25),
              ('C', 'D', 14),
              ('D', 'A', 18)}

graph.add_weighted_edges_from(kilometres)


print(graph.edges)
nx.draw_circular(graph,
                 node_color='red',
                 node_size=1000,
                 with_labels=True)
plt.show()
