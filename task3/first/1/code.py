import numpy as np
import pylab as plt

data = np.loadtxt('log.lammps', skiprows=98)

fig, ax = plt.subplots(figsize=(10,10))

ax.scatter(data[::5,0], data[::5,1], color='blue', label='forward', lw=3)
plt.grid()
plt.legend()
plt.xlabel('Temperature', fontsize=20)
plt.ylabel('Total Energy', fontsize=20)
plt.title('Observation of a phase transition from a total energy jump \n ($\\rho$ = 1.0, dt = 0.001, N = 6912)', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
fig.savefig('plot10.pdf')
