import networkx as nx

ranked_node_names = [['start'],
                     [1, 2, 3],
                     ['a', 'b', 'c'],
                     ['end']]
node_edges = [('start', 2),
              ('start', 3),
              (2, 'b'),
              ('b', 'end'),
              ('a', 'end')]

# graph and base nodes/edges in networkx
G = nx.DiGraph()
for rank_of_nodes in ranked_node_names:
    G.add_nodes_from(rank_of_nodes)
G.nodes(True)
G.add_edges_from(node_edges)
# I don't know a way to automatically arrange in networkx so using graphviz
A = nx.to_agraph(G)
A.graph_attr.update('LR')  # change direction of the layout
for rank_of_nodes in ranked_node_names:
    A.add_subgraph(rank_of_nodes, 'same')
# draw
A.draw('example.png', 'dot')