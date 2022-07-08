import numpy as np

De = []
Dg = []
t = 0.001*10000
dt = 0.001*100

for i in range(1,6):
    S = 0
    data = np.loadtxt('log'+str(i)+'.txt')
    De.append(data[-1][0]/6/t)
    for ac in data[:,1]:
        S += ac*dt
    Dg.append(S/3)
    
Dg = np.array(Dg)
De = np.array(De)
print('De: ',np.mean(De), '; Dg: ', np.mean(Dg))
