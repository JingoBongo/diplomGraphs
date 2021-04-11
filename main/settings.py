import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import datetime
import json
from networkx.readwrite import json_graph

whileBool = True
successfulCommand = False
requires_saving = False
requires_saving_json = False
requires_saving_gexf = False
draw_plot = True
graph = nx.Graph()
figure = None
filename = ''