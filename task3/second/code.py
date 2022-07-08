import numpy as np
import pylab as plt

data = np.loadtxt('log.lammps', skiprows=96)

fig, ax = plt.subplots(figsize=(15,12))

ax.scatter(data[:1100,0], data[:1100,5]/0.794, color='blue', label='forward',lw=3)
ax.hlines(0.12, 1.2, 1.7, color='black', lw=3, linestyles="--")
plt.grid()
plt.legend()
plt.xlabel('Temperature', fontsize=20)
plt.ylabel('Lindemann criteria', fontsize=20)
plt.title('Observation of a phase transition from Lindemann criteria ($\\rho$ = 1.0, dt = 0.001, N = 6912)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
fig.savefig('plot.pdf')
