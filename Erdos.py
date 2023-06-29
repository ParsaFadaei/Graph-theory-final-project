import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import pandas as pd
import math
import seaborn as sns

import functions

simulationCount = 500
count = 24
currentRow = 0
data = {
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0,
    26: 0,
    28: 0,
    29: 0,
    30: 0,
    40: 0,
    50: 0,
}
df = pd.DataFrame(list(data.items()), columns=['Size', 'OC'])
# df['Percent'] = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%']
graphSizes = list(data.keys())
while count > 0:
    print(count)
    graphER = list()
    i = 0
    while i < simulationCount:
        size = graphSizes[currentRow]
        avg_degree = math.sqrt(size)
        edges = size * avg_degree / 2
        max_edge = size * (size - 1) / 2
        p = edges / max_edge
        # p = math.sqrt(size) / (size - 1)
        graphER.append(nx.erdos_renyi_graph(size, p))
        i += 1

    for g in graphER:
        if functions.isOC(g):
            df.loc[currentRow, 'OC'] += 1

    currentRow += 1
    count -= 1

df['OC %'] = df.apply(lambda row: row.OC / simulationCount * 100, axis=1)
print(df)
# df.plot(kind='bar', x='Size', y='OC %')
"""SHOW USING SEABORN"""
sns.regplot(x=df['Size'], y=df['OC %'])
plt.show()
"""SHOW USING MATPLOTLIB"""
# b, m = polyfit(df['Size'], df['OC %'], 1)
# plt.scatter(df['Size'], df['OC %'], c='r')
# plt.plot(df['Size'], b + m * df['Size'], '-')
# plt.xlabel('Size')
# plt.ylabel('OC %')
# plt.title('OC percentage for ER graphs')
# plt.show()
