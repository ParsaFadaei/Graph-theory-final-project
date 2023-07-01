import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

import functions
import LayeredGraph

""""PART 3 ,5, 6"""
# erdos = nx.erdos_renyi_graph(30, p=0.3)
# tetra = nx.tetrahedral_graph()
# octa = nx.octahedral_graph()
# cube = nx.cubical_graph()
# ico = nx.icosahedral_graph()
# truncTetra = nx.truncated_tetrahedron_graph()
# hyperCube = nx.hypercube_graph()
# Torus = nx.complete_graph(7)
ring = functions.ring_graph(10, 1)
# prism3 = functions.schlegel3Prism()
# Antiprism3 = functions.schlegel3Antiprism()
# Twistedprism3 = functions.sclegel3TwistedPrism()
# completeN = nx.complete_graph(8)
# hamming = functions.hamming_binary(4)



G = ring
# H = prism3
# functions.setAllCaps(G)


functions.getInfo(G)

""""CALCULATING L"""
# L = float(0)
# newL = float(0)
# L = functions.calculateLHamming(G)
# L = functions.calculateLforSymm(G)
# L = functions.calculateL(G)
# L = functions.calculateLmax(G)

# functions.remove_rnd_node(G, 0.2)
# newL = functions.calculateLHamming(G)
# newL = functions.calculateLforSymm(G)
# newL = functions.calculateL(G)
# newL = functions.calculateLmax(G)
# increasePerc = functions.changePerc(newL, L)

# print("INCREASE Perc =", increasePerc, "%")
"""PART 7 & 8"""

# T = functions.createLayeredGraph(G, H);
# functions.show3dSpring(T)


""""SHOWING THE GRAPHS"""
# functions.show3dSpring(G)
# nodePos = nx.planar_layout(G)
# nodePos = nx.shell_layout(G)
# nodePos = nx.spectral_layout(G)
# nodePos = nx.spiral_layout(G)
# nodePos = nx.onion_layers(G)
# nx.draw(hamming, nodePos)
# plt.show()




