import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_node(0, weight=8)
G.add_node(1, weight=5)
G.add_node(2, weight=3, color = 'green')
# labels = {n: G.nodes[n]['weight'] for n in G.nodes}
labels = {
    n: str(n) + '\nweight=' + str(G.nodes[n]['weight']) if 'weight' in G.nodes[n] else str(n)
    for n in G.nodes
}

colors = [G.nodes[n]['weight'] for n in G.nodes]
print(labels)
print('popopopopopopopo')
print(colors)
print(G.nodes.get(2))
nx.draw(G, with_labels=True, labels=labels, node_color=colors)
plt.show()