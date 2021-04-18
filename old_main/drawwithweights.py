import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import datetime

whileBool = True
successfulCommand = False
requires_saving = False
graph = nx.Graph()

kilometres = {('A', 'B', 15),
              ('B', 'C', 16),
              ('B', 'D', 25),
              ('C', 'D', 14),
              ('D', 'A', 18)}



# graph.add_weighted_edges_from(kilometres)
graph.add_node('A', weight=5, pos=(1,1))
graph.add_node('B', pos=(2,2))
graph.add_edge('A','B', weight = 6)


labels = nx.get_edge_attributes(graph, 'weight')

# nx.draw(graph,
#         node_color='red',
#         node_size=1000,
#         edge_labels=labels)
pos = nx.get_node_attributes(graph, 'pos')
nx.draw_circular(graph,
                 node_color='red',
                 node_size=1000,
                 with_labels=True,)
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
# plt.ion()
# plt.pause(0.001)
# plt.show()
# plt.clf()

print(graph.get_edge_data('A', 'B'))
print(graph.get)