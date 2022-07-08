import numpy as np
import pylab as plt
from scipy.optimize import fsolve
import scipy as sp

plt.figure(figsize=(15, 12))

gs = np.loadtxt('sol0', skiprows=2)
for i in range(1, 21):
    gs += np.loadtxt('sol'+str(i), skiprows=2)
    

gp = np.loadtxt('ph145', skiprows=2)
for i in range(146, 166):
    gp += np.loadtxt('ph'+str(i), skiprows=2)


gl = np.loadtxt('liq180', skiprows=2)
for i in range(181, 201):
    gl += np.loadtxt('liq'+str(i), skiprows=2)
gl = gl/21
gp = gp/21
gs = gs/21
x = gl.T[0]
    

plt.tick_params(axis='both', which='major', labelsize=16)
plt.plot(gl.T[1], color='red', label='liquid (T $\\approx 2.8$)', lw=3)
plt.plot(gp.T[1], color='blue', label='phase transition (T $\\approx 2.6$)', lw=3)
plt.plot(gs.T[1], color='green', label='solid (T$\\approx 2.2$)', lw=3)
plt.legend(fontsize=16)
plt.xlabel('Pair separation distance', fontsize=20)
plt.ylabel('g(r)', fontsize=20)
plt.grid()
plt.show()
