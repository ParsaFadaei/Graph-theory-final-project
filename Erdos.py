import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd
import math

import functions

simulationCount = 100
count = 13
currentP = 0.1
currentRow = 0
data = {
    7: 0,
    9: 0,
    10: 0,
    14: 0,
    16: 0,
    18: 0,
    20: 0,
    25: 0,
    30: 0,
    50: 0,
    100: 0,
    300: 0,
    500: 0,
}
df = pd.DataFrame(list(data.items()), columns=['n', 'OC'])
# df['Percent'] = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%']
graphSizes = list(data.keys())
while count > 0:
    graphER = list()
    i = 0
    while i < simulationCount:
        size = graphSizes[currentRow]
        p = math.sqrt(size) / (size - 1)
        graphER.append(nx.erdos_renyi_graph(size, p))
        i += 1

        for g in graphER:
            if functions.isOC(g):
                df.loc[currentRow, 'OC'] += 1

    currentRow += 1
    count -= 1

df['OC Perc'] = df.apply(lambda row: row.OC/simulationCount * 100, axis=1)
print(df)