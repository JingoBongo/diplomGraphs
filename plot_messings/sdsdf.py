import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(4)  # or DiGraph, etc
G.remove_edge(0, 1)
# e = (1, 2)
# G.remove_edge(*e)  # unpacks e from an edge tuple
# e = (2, 3, {"weight": 7})  # an edge with attribute data
# G.remove_edge(*e[:2])
nx.draw(G, pos=nx.planar_layout(G))
plt.show()
