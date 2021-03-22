import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation
import matplotlib

matplotlib.use('TkAgg')

H = nx.from_edgelist([(0, 1), (1, 2), (0, 2), (1, 3)])
pos = nx.spring_layout(H, iterations=200)

# here goes your statuses as a list of lists
statuses = [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1]]
colors = {0: 'red', 1: 'green', 2: 'blue', 3: 'black'}

# create a generator from your statuses
# which yields the corresponding color map for each new status
def status():
    for s in statuses:
        yield list(map(lambda x: colors[x], s))  # map statuses to their colors

color_map = status()
print(color_map)
print(statuses)
print(colors)

def draw_next_status(n):
    plt.cla()
    c_map = next(color_map, colors.values())
    nx.draw(H, pos, node_color=c_map, node_size=700, with_labels=True, edge_color='green')


ani = animation.FuncAnimation(plt.gcf(), draw_next_status, interval=1000, frames=len(statuses), repeat=False)

plt.show()