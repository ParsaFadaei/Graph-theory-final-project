import matplotlib
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import logging
import matplotlib.colors as mcolors
import re
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

colors = mcolors.CSS4_COLORS.keys()


def show3dSpring(G):
    pos = nx.spring_layout(G, dim=3, seed=779)
    # Extract node and edge positions from the layout
    node_xyz = np.array([pos[v] for v in sorted(G)])
    edge_xyz = np.array([(pos[u], pos[v]) for u, v in G.edges()])

    # Create the 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot the nodes - alpha is scaled by "depth" automatically
    ax.scatter(*node_xyz.T, s=100, ec="w")

    # Plot the edges
    for vizedge in edge_xyz:
        # ax.plot(*vizedge.T, color="tab:gray")
        ax.plot(*vizedge.T)

    _format_axes(ax)
    fig.tight_layout()
    plt.show()


def _format_axes(ax):
    """Visualization options for the 3D axes."""
    # Turn gridlines off
    ax.grid(True)
    # Suppress tick labels
    for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
        dim.set_ticks([])
    # Set axes labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


def isIsomorphic(G1, G2):
    return nx.vf2pp_is_isomorphic(G1, G2, node_label=None)


def getInfo(G):
    nodeNum = nx.number_of_nodes(G)
    print("nodes:" + str(nodeNum))
    print("edges:" + str(nx.number_of_edges(G)))
    minDeg = minDegree(G)
    print("min Degree:" + str(minDeg))
    k = nx.node_connectivity(G)
    lam = nx.edge_connectivity(G)
    print("K:" + str(k))
    print("lambda:" + str(lam))
    isOC = False
    isNS = False
    if k == lam == minDeg:
        isOC = True
        print("OC:" + str(isOC))

    if lam == minDegree and k >= 2 * (minDeg + 1) / 3:
        isNS = True
        if 4 >= minDeg:
            if minDegree != k:
                isNS = False
        if isIsomorphic(G, G):
            if k == minDeg:
                isNS = True
        print("NS:" + str(isNS))


def isOC(G):
    minDeg = minDegree(G)
    k = nx.node_connectivity(G)
    lam = nx.edge_connectivity(G)
    print(minDeg, k, lam)
    if k == lam == minDeg:
        return True
    else:
        return False


def isNS(G):
    isNS = False
    minDeg = minDegree(G)
    k = nx.node_connectivity(G)
    lam = nx.edge_connectivity(G)
    if lam == minDegree and k >= 2 * (minDeg + 1) / 3:
        isNS = True
        if 4 >= minDeg:
            if minDegree != k:
                isNS = False
    return isNS


def minDegree(G):
    minDeg = min([val for (node, val) in G.degree()])
    return minDeg


def schlegel3Prism():
    g = nx.Graph()
    g.add_nodes_from([0, 5])
    g.add_edges_from([(0, 1), (0, 2), (1, 2), (0, 3), (2, 5), (1, 4), (3, 5), (3, 4), (4, 5)])
    return g


def schlegel3Antiprism():
    g = nx.Graph()
    g.add_nodes_from([0, 5])
    g.add_edges_from([(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 5), (0, 5), (1, 4), (2, 4), (3, 5), (3, 4), (4, 5)])
    return g


def sclegel3TwistedPrism():
    g = nx.Graph()
    g.add_nodes_from([0, 5])
    g.add_edges_from([(0, 1), (0, 2), (1, 2), (0, 3), (0, 4), (2, 5), (2, 3), (1, 4), (1, 5), (3, 5), (3, 4), (4, 5)])
    return g


def ring_graph(n, k):
    graph = nx.Graph()

    for i in range(n):
        sources = [i] * k
        targets = range(i + 1, i + k + 1)
        targets = [node % n for node in targets]
        graph.add_edges_from(zip(sources, targets))

    return graph


def hamming_binary(chromosome_len):
    space = nx.Graph()

    # create all nodes
    all_nodes = range(0, 2 ** chromosome_len)
    space.add_nodes_from(all_nodes)

    # for each node, find neighbors
    for node in space.nodes():
        [space.add_edge(node, mutate_node(node, base)) for base in range(chromosome_len)]
    return space


def mutate_node(node, n):
    return node ^ (1 << n)


def avgDistHamming(d, q):
    return (d * (q - 1) * (q ** (d - 1))) / (q ** d) - 1


def chromaticNumber(G):
    return max(nx.greedy_color(G, 'random_sequential', colors).values()) + 1


def calculateLHamming(G):
    n = nx.number_of_nodes(G)
    d = nx.diameter(G)
    q = chromaticNumber(G)
    minDeg = minDegree(G)
    avg = avgDistHamming(d, q)
    L = (n - 1) * avg / minDeg
    print("L Hamming:" + str(L))
    return float(L)


def calculateLforSymm(G):
    n = nx.number_of_nodes(G)
    minDeg = minDegree(G)
    avg = nx.average_shortest_path_length(G)
    L = (n - 1) * avg / minDeg
    print("L Symmetric:" + str(L))
    return float(L)


def setAllCaps(G):
    nx.set_edge_attributes(G, 20.0, "capacity")


def calculateL(G):
    source = min(G.nodes())
    sink = max(G.nodes())
    # Compute the maximum flow value using the Edmonds-Karp algorithm
    flow_value = nx.maximum_flow_value(G, source, sink)
    print("L value (networkx): " + str(flow_value))
    return float(flow_value)


def calculateLmax(G):
    source = min(G.nodes())
    sink = max(G.nodes())
    # Edmonds-Karp algorithm
    flow_value = nx.maximum_flow_value(G, source, sink)
    # Stoer-Wagner algorithm
    cut_value, partition = nx.stoer_wagner(G)
    # Compute the maximum flow value using the max-flow min-cut theorem
    max_flow_value = cut_value + flow_value
    print("Maximum flow value (mincut theorem): ", max_flow_value)
    return float(max_flow_value)


def remove_rnd_node(G, p=0.2):
    for node in list(G.nodes()):
        if random.random() < p:
            G.remove_node(node)


def changePerc(new_value, old_value):
    return ((new_value - old_value) / abs(old_value)) * 100


def createLayeredGraph(G, H, p=0.1):
    U = nx.disjoint_union(G, H)
    for i, g in enumerate(U.nodes()):
        for j, h in enumerate(U.nodes(), len(G)):
            if i < len(G) - 1:
                if random.random() < p:
                    U.add_edge(g, h, color='red')

    return U
