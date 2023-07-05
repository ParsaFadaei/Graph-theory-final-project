import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import functions


erdos = nx.erdos_renyi_graph(1000, p=0.3)



G = erdos


k= nx.node_connectivity(G)
if k ==3:
    lam = nx.edge_connectivity(G)
    minDeg = functions.minDegree(G)
    if k == lam == minDeg:
        H = nx.scale_free_graph(2)
    else:
        print("Failed")

if H is not None:
    print("Creating multilayer")
    T = functions.createLayeredGraph(G, H)
    functions.getInfo(T)
    functions.show3dSpring(T)



"""PART 7 & 8"""


