import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

data1 = np.loadtxt('log1.txt')
data2 = np.loadtxt('log2.txt')
data3 = np.loadtxt('log3.txt')
data3 = np.loadtxt('log4.txt')

x= np.linspace(0, 1, 100)
fig, ax = plt.subplots()  # Create a figure containing a single axes
ax.plot(data1[:,0],  label='$\\tau$ = 1 ' )  # Plot some data on the axes.
ax.plot(data2[:,0],  label='$\\tau$ = 10 ' )  # Plot some data on the axes.
ax.plot(data3[:,0],  label='$\\tau$ = 20 ' )  # Plot some data on the axes.
ax.plot(data3[:,0],  label='$\\tau$ = 50 ' )  # Plot some data on the axes.

#ax.plot(x, arr1, 'x-', label='T=1.2 p=0.85' )  # Plot some data on the axes.
ax.set_xlabel('0.1*t')  # Add an x-label to the axes.
#ax.set_ylabel('rdf')  # Add a y-label to the axes.
ax.set_title("MSD rho=0.7 dt=0.001")
ax.grid(color='black', linestyle='-')
ax.legend()  # Add a legend.
plt.show()
fig.savefig('tau.png')
