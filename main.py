import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import functions

tetra = nx.tetrahedral_graph()
octa = nx.octahedral_graph()
cube = nx.cubical_graph()
ico = nx.icosahedral_graph()
truncTetra = nx.truncated_tetrahedron_graph()
hyperCube = nx.hypercube_graph()
# functions.show3dSpring(tetra)
functions.getInfo(tetra)
