import numpy as np
import pylab as plt
import json

filename = '_slurm-out.txt'

data = np.genfromtxt(filename, skip_header=11)
data = data[:, 2]

data = data[1000:]

variances = []
means = []
variances.append(np.var(data) / len(data))
means.append(np.mean(data))
variances, means

from IPython.display import clear_output
from time import sleep

for line in range(2,10000,100):
    stop = data.shape[0] // line * line
    nblocks = data.shape[0] // line
    new_data = np.zeros(nblocks)
    for block in range(nblocks):
    	new_data[block] = sum(data[block*line:(block+1)*line])/line
    variances.append(np.var(new_data)/(len(new_data) - 1))
    means.append(np.mean(new_data))

data = {}
data['variances'] = variances
data['means'] = means

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

fig, ax = plt.subplots()
x = np.linspace(2, 2 + (100*101), 101, False)
ax =plt.plot(variances)
fig.savefig('fig.png')
