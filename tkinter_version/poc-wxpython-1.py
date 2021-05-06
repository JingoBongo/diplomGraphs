import wx
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas


class NetworkFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1)
        self.SetSize(wx.Size(1280, 768))

        self.panel = wx.Panel(self)
        self.fig = plt.figure()
        self.canvas = FigCanvas(self.panel, -1, self.fig)

        G = nx.Graph()

        nodes = [0, 1, 2, 3, 4, 5, 6, 7]
        node_sizes = [6500, 4000, 4000, 2500, 2500, 2500, 2500, 2500]
        node_color = ["#00d992", "#00d9c8", "#00d9c8", "#00b4d9", "#00b4d9", "#00b4d9", "#00b4d9", "#00b4d9"]
        edges = [(1, 0), (2, 0), (3, 1), (4, 1), (5, 1), (6, 2), (7, 2)]
        node_label = {0: "Printer",
                      1: "Case",
                      2: "Electronics",
                      3: "Plastic 1",
                      4: "Plastic 2",
                      5: "Plastic 3",
                      6: "Metal 1",
                      7: "Metal 2"}

        edge_weights = [1, 0.5, 0.5, 0.1, 0.1, 0.1, 0.1, 0.1]  # ?????

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)

        nx.draw(G, node_size=node_sizes, node_color=node_color, labels=node_label, with_labels=True)

        plt.axis('off')

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.panel.SetSizer(self.vbox)


if __name__ == '__main__':
    app = wx.App()
    app.frame = NetworkFrame()
    app.frame.Show()
    app.MainLoop()