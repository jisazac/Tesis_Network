import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
H=nx.path_graph(10)
G.add_nodes_from(H)
G.add_edge(1,2)
e=(2,3)
G.add_edge(*e) # unpack edge tuple*
G.add_edges_from([(1,2),(1,3)])
nx.draw_random(G)
plt.show()


M=nx.Graph()
M.add_node(1, time='5pm')
M.add_nodes_from([3], time='2pm')


M.node[1]['room'] = 714
M.nodes(data=True)
nx.draw_random(M)
plt.show()
