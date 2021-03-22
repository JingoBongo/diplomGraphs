import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()

g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('d', 'b')
g.add_node('f')

pos=nx.spring_layout(g)
plt.figure(figsize=(5,5))
nx.draw_networkx_nodes(g, pos)
nx.draw_networkx_edges(g, pos,width=0.5, node_size=500, edge_color='green')
# nx.draw_networkx_labels(g, pos, with_lables=False)
plt.axis('off')
plt.show()