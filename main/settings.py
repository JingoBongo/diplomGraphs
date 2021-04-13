import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import datetime
import json
from networkx.readwrite import json_graph
from matplotlib.widgets import Button
import math

whileBool = True
successfulCommand = False
requires_saving = False
background_is_image = False
requires_saving_json = False
requires_saving_gexf = False
draw_plot = True
graph = nx.Graph()
draw_style = 'planar'
filename = ''
default_node_color = 'yellow'
default_wh_color = 'green'
generic_node_name = 'n'
generic_node_name_counter = 0
background_img = None
fullscreen = False
show_weight_labels = True
proportion = None
# proportion is what we multiply to.... in progress

# experimental vars
ax = None
figure = None