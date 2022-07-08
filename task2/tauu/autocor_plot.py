import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

props = dict(boxstyle='round', facecolor='wheat', alpha=0.7)

'''
arr = []
with open("difffusion1.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(float(line)/20.0)
'''
ddrr1 = []
with open("SKS1.txt") as f:
        for line in f:
            #print(float(x) for x in coloumn.split())
            ddrr1.append(line.split())
r1 = []
t = []
for i in range(len(ddrr1)):
    t.append(float(ddrr1[i][0])*0.001)
    r1.append(float(ddrr1[i][1])**2)

n = len(t)
st = int(round(0.7*n, 0))
print(st)
z1 = np.polyfit(t[st:], r1[st:], 1)
f1 = np.poly1d(z1)   




ddrr2 = []
with open("SKS10.txt") as f:
        for line in f:
            #print(float(x) for x in coloumn.split())
            ddrr2.append(line.split())
r2= []
for i in range(len(ddrr2)):
    r2.append(float(ddrr2[i][1])**2)
z2 = np.polyfit(t[st:], r2[st:], 1)
f2 = np.poly1d(z2)





ddrr3 = []
with open("SKS100.txt") as f:
        for line in f:
            #print(float(x) for x in coloumn.split())
            ddrr3.append(line.split())
r3= []
for i in range(len(ddrr3)):
    r3.append(float(ddrr3[i][1])**2)
z3 = np.polyfit(t[st:], r3[st:], 1)
f3 = np.poly1d(z3)




name1 = 'D($\\tau$ = 1) = %g' % round(z1[0]/6.0, 3)
print(name1)


name2 = 'D($\\tau$ = 10) = %g' % round(z2[0]/6.0, 3)
print(name2)

name3 = 'D($\\tau$ = 100) = %g' % round(z3[0]/6.0, 3)
print(name3)


fig, ax = plt.subplots()  # Create a figure containing a single axes

ax.plot(t[:n], r1[:n], label='$\\tau$=1' )  # Plot some data on the axes.
ax.plot(t[st:], f1(t[st:]))
ax.plot(t[:n], r2[:n], label='$\\tau$=10' )
ax.plot(t[st:], f2(t[st:]))
ax.plot(t[:n], r3[:n], label='$\\tau$=100' )
ax.plot(t[st:], f3(t[st:]))

#dd.text(0, 0.95*max(ddx), name, fontsize = 14, verticalalignment='top',  bbox=props)

ax.text(22, 13, name1, fontsize = 10, bbox=props)
ax.text(22, 10, name2, fontsize = 10, bbox=props)
ax.text(22, 7, name3, fontsize = 10, bbox=props)

#ax.plot(x, arr1, 'x-', label='T=1.2 p=0.85' )  # Plot some data on the axes.
ax.set_xlabel('t')  # Add an x-label to the axes.
ax.set_ylabel('<r^2>')  # Add a y-label to the axes.
ax.set_title("MSD from Lagngevin's $\\tau$ thermostat dt = 0.001, rho = 0.7, T = 2.0")
ax.grid(color='black', linestyle='-')
ax.legend()  # Add a legend.




plt.show()

