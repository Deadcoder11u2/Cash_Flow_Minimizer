import matplotlib.pyplot as plot
import networkx as nx
import os
import time

os.system("java Minimize")
time.sleep(1)
output = open("output.txt", "r")
nodes, edges = map(int, output.readline().split())
l = []
for i in range(1, nodes): 
    l.append(i)

G = nx.DiGraph()
G.add_nodes_from(l)
for i in range(edges):
    u, v, debt = map(float, output.readline().split())
    G.add_edge(int(u), int(v), length = debt)
nx.is_weighted(G)
pos = nx.spring_layout(G)


nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos)
plot.savefig("fig1.png")
