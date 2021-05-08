import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import datetime
import json
from networkx.readwrite import json_graph
from matplotlib.widgets import Button
import math
import re
from os.path import abspath
from os.path import basename
from inspect import getsourcefile
from os import getcwd

whileBool = True
successfulCommand = False
requires_saving = False
background_is_image = False
requires_saving_json = False
requires_saving_gexf = False
draw_plot = True
graph = nx.Graph()
draw_style = 'none'
filename = ''
default_node_color = 'yellow'
default_wh_color = 'green'
generic_node_name = 'n'
generic_node_name_counter = 0
background_img = None
fullscreen = False
show_weight_labels = False
# =========== proportion section =======================
proportion = None
default_edge_value = 'dist'
edge_value = 'dist'  # another possibility : metric
prop_d = 1
prop_m = 1
prop_m_suffix = 'm'
# and array of 2 for creating edge
mouse_clicked_nodes = []
distance_out_loud = False
# proportion logic: new edge's weight in metric system = ( prop_m * edge dist )/prop_d ; and by default I want to keep it 1:1

# experimental vars
ax = None
figure = None


def cust_print(self, message):
    if not message:
        message = 'error'
    print(str(message))
    self.console_output.append(str(message))
