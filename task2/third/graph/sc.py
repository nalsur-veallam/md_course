import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

data2 = np.loadtxt('log4.txt')

dt = 0.01*100
integral = []
integ = 0
integral.append(integ)
for i in data2[:,1]:
    integ += i*dt
    integral.append(integ)

x= np.linspace(0, 200, 202)
fig, ax = plt.subplots()  # Create a figure containing a single axes
ax.plot(x, integral[:202],  label='T=1 ' )  # Plot some data on the axes.

#ax.plot(x, arr1, 'x-', label='T=1.2 p=0.85' )  # Plot some data on the axes.
ax.set_xlabel('t')  # Add an x-label to the axes.
#ax.set_ylabel('rdf')  # Add a y-label to the axes.
ax.set_title("Convergence of the autocorrelator integral rho=0.7 dt=0.001")
ax.grid(color='black', linestyle='-')
ax.legend()  # Add a legend.
plt.show()
fig.savefig('conv.png')
