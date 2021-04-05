import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
i=1
G.add_node(i,pos=(i,i), name = i)
G.add_node('B',pos=(4,4), weight=5, name = 'B')
G.add_node(2,pos=(2,2), name = 2)
G.add_node(3,pos=(1,0), name = 3)
G.add_edge(1,2,weight=0.5)
G.add_edge(1,3,weight=9.8)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nd_labels = nx.get_node_attributes(G, 'name')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw_networkx_labels(G, pos, labels=nd_labels)

# 2nd implementation
# node_labels = nx.get_node_attributes(G,'state')
# nx.draw_networkx_labels(G, pos, labels = node_labels)
# edge_labels = nx.get_edge_attributes(G,'state')
# nx.draw_networkx_edge_labels(G, pos, labels = edge_labels)

# nx.draw_networkx_nodes(G, pos, nodelist=nx.nodes(G), with_labels=True)

print(G.graph)
print('=======')
for i in G.nodes:
    print()
print(G.nodes['B'])
plt.show()

# so, what is a must from here:
# 1. adding node names together with adding nodes, TODO same for removing?
# 2. drawing in several commands, default DRAW, then DRAW_EDGE_LABELS, then DRAW_NETW_LABELS for nodes
# 3. default color of all nodes = red, solution will be a green, yellow, etc. but default is red
# 4. position, i want to try string positioning
# 5. it will be a distinct func, together with having local vars for arrays with params probably