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
        ax.plot(*vizedge.T, color="tab:gray")

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


def minDegree(G):
    minDeg = 0
    degrees = [val for (node, val) in G.degree()]
    for d in degrees:
        if d > minDeg:
            minDeg = d
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
    logging.debug(all_nodes)
    space.add_nodes_from(all_nodes)

    # for each node, find neighbors
    for node in space.nodes():
        [space.add_edge(node, mutate_node(node, base)) for base in range(chromosome_len)]
    return space


def mutate_node(node, n):
    return node ^ (1 << n)


def avgDist(d, q):
    return (d * (q - 1) * (q ** (d - 1))) / (q ** d) - 1


def chromaricNumber(G):
    return max(nx.greedy_color(G, 'random_sequential', colors).values()) + 1


def calculateL(G):
    n = nx.number_of_nodes(G)
    d = nx.diameter(G)
    q = chromaricNumber(G)
    minDeg = minDegree(G)
    avg = avgDist(d, q)
    return (n - 1) * avg / minDeg
