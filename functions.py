import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


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


def getInfo(G):
    nodeNum = nx.number_of_nodes(G)
    print("nodes:" + str(nodeNum))
    print("edges:" + str(nx.number_of_edges(G)))
    minDegree = 0
    degrees = [val for (node, val) in G.degree()]
    for d in degrees:
        if d > minDegree:
            minDegree = d
    print("min Degree:" + str(minDegree))
    k = nx.node_connectivity(G)
    lam = nx.edge_connectivity(G)
    print("K:" + str(k))
    print("lambda:" + str(lam))
    isOC = False
    isNS = False
    if k == lam == minDegree:
        isOC = True
        print("OC:" + str(isOC))

    if lam == minDegree and k >= 2 * (minDegree + 1) / 3:
        if 4 >= minDegree == k:
            isNS = True
        else:
            # check is symmetric
            isNS = True

        print("NS:" + str(isNS))
