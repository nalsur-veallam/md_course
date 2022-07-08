import numpy as np
import pylab as plt

data1 = np.loadtxt('log.lammps', skiprows=0)
data2 = np.loadtxt('log3.lammps', skiprows=723)

fig, ax = plt.subplots(figsize=(15,12))

ax.scatter(data1[::10,0], data1[::10,3], color='blue', label='forward')
ax.scatter(data2[::10,0], data2[::10,3], color='gold', label ='backward')
plt.grid()
plt.legend()
plt.xlabel('Temperature')
plt.ylabel('Density')
plt.title('Observation of a phase transition from a density jump (P = 10, dt = 0.001, N = 7000)')
plt.show()
fig.savefig('plot101.png')
