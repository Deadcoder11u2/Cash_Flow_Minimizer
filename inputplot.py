from matplotlib.patches import FancyArrow
import matplotlib.pyplot as plt
import networkx as nx
from networkx.classes.function import edges

f = open("input.txt", "r")
nodes, edges = map(int, f.readline().split())
G = nx.DiGraph()
l = list(range(nodes))

ed_list = []
G.add_nodes_from(l)
for i in range(edges):
    u, v, debt = map(float, f.readline().split())
    G.add_edge(u, v, len = debt)
pos = nx.spring_layout(G)


nx.is_weighted(G)
pos = nx.spring_layout(G)


nx.draw_networkx_nodes(G, pos, node_size=700, node_color='red')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', arrowsize=20)
nx.draw_networkx_labels(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos)
plt.savefig("fig2.png")