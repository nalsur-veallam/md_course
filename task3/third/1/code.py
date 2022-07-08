import numpy as np
import pylab as plt

data = np.loadtxt('log.lammps', skiprows=96)

fig, ax = plt.subplots(figsize=(15,12))

ax.hist(data, bins=100, range=(0.00725,0.00875))
plt.title('Distribution of deviation from the equilibrium position ($\\rho$ = 1.0, T = 1.0, dt = 0.001, N = 7000)')
plt.show()
fig.savefig('plot.pdf')
