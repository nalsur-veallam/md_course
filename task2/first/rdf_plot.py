import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)



arr = []
with open("rdf.txt") as f:
    for line in f:
        if line.split()[0]=='#': continue 
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
x = []
y = []

for i in range(len(arr)):
    x.append(float(arr[i][0]))
    y.append(float(arr[i][1]))




fig, ax = plt.subplots()  # Create a figure containing a single axes

ax.plot(x, y,'o-', label='rdf' )  # Plot some data on the axes.
ax.set_xlabel('r')  # Add an x-label to the axes.
ax.set_ylabel('rdf')  # Add a y-label to the axes.
ax.set_title("RDF (gas)")
ax.legend()  # Add a legend.



plt.show()
'''

    print(sum(en)/len(en), "en")
    print(sum(p[-200:])/(200), "p")
    print(sum(d[-200:])/(200), "<KE/TE>")
    print(sum(c[-200:])/(200), "pk/p")
   

'''


