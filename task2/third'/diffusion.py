import numpy as np

De = []
Dg = []
n = 40000
t = 0.001*1000
dt = 0.001*20

for i in range(100):
    for j in range(51):
        data = np.loadtxt('dump.'+str(n+100*i+j*20), skiprows=9)
        De.append((data[-1][1] - data[0][1])**2 + (data[-1][2] - data[0][2])**2 + (data[-1][3] - data[0][3])**2)/6/t
        Dg.append()
        
