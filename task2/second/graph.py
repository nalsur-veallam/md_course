import numpy as np
import pylab as plt


data = np.loadtxt('log.lammps', skiprows=523)

acfs = data[:,1]

plt.plot(acfs)
plt.xlabel('dt*100')
plt.title('Autocorrelator')
plt.show()
