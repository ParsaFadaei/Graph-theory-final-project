import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import pandas as pd
import math
import seaborn as sns

import functions


G = nx.erdos_renyi_graph(10, 0.4)
minDeg = min([node for (node, val) in G.degree()])
minDeg2 = min([val for (node, val) in G.degree()])
print(minDegree)
# print(minDeg, " 2:", minDeg2)
# print(functions.isOC(G))

def minDegree(G,x):
    minDeg = G.degree[0]
    for y in range(x):
        if G.degree[y] < minDeg:
            minDeg = G.degree[y]
    return minDeg