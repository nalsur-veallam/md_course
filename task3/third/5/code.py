import numpy as np
import pylab as plt

data_0 = np.loadtxt('dump.0', skiprows=9)
data = np.loadtxt('dump.20000', skiprows=9)

data = data[np.argsort(data[:, 0])]

data = data-data_0
datax = data[:,1]
data = np.sqrt((data[:,1]**2 + data[:,2]**2 + data[:,3]**2))
print(np.shape(data))
fig, ax = plt.subplots(figsize=(15,15))

ax.hist(data, bins=100, range=(0,0.3))
plt.tick_params(axis='both', which='major', labelsize=16)
plt.title('Distribution of deviation from the equilibrium position ($\\rho$ = 1.2, T = 1.0, dt = 0.001, N = 4000000)', fontsize=20)
plt.show()
fig.savefig('hist.pdf')

fig, ax = plt.subplots(figsize=(15,15))

ax.hist(datax, bins=100, range=(-0.3,0.3))
plt.tick_params(axis='both', which='major', labelsize=16)
plt.title('Distribution of deviation (only for x axis) from the equilibrium position ($\\rho$ = 1.2, T = 1.0, dt = 0.001, N = 4000000)', fontsize=20)
plt.show()
fig.savefig('histx.pdf')
