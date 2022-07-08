import numpy as np

De = []
t = 0.001*10000

for i in range(1,5):
    S = 0
    data = np.loadtxt('log'+str(i)+'.txt')
    De.append(data[-1][0]/6/t)
    

print('De: ',De)
