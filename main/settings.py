import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import datetime
import json
from networkx.readwrite import json_graph
from matplotlib.widgets import Button

whileBool = True
successfulCommand = False
requires_saving = False
requires_saving_json = False
requires_saving_gexf = False
draw_plot = True
graph = nx.Graph()
figure = None
draw_style = 'planar'
filename = ''
default_node_color = 'blue'
default_wh_color = 'green'
generic_node_name = 'N'
generic_node_name_counter = 0
background_img = None