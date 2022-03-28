import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

N = 216
P = []
Pk = []
rho = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
rho_ = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

for i in range (1, 10):
	data = np.loadtxt('0_' + str(i) + '.txt', skiprows = 11)
	p = data[:,7]
	P.append(np.mean(p[len(p) - 100 : len(p)]))
	Pk.append(2*rho[i-1]*data[-1,3]/3/N)
	
data = np.loadtxt('1_0.txt', skiprows = 11)
p = data[:,7]
P.append(np.mean(p[len(p) - 100 : len(p)]))
Pk.append(2*1.0*data[-1,3]/3/N)

plt.plot(rho, P, '.-')
plt.title('pressure from density')
plt.xlabel('density')
plt.ylabel('pressure')
plt.show()
clear_output()

b = []

for i in range(0, 9):
	b.append(0.1/(P[i+1] - P[i])/rho[i])
	
plt.plot(rho_, b, '--')
plt.scatter(rho_, b)
plt.title('compressibility from density')
plt.xlabel('density')
plt.ylabel('compressibility')
plt.show()
clear_output()

pd = []
for i in range(0,10):
	pd.append(Pk[i]/P[i])

plt.scatter(rho, pd)
plt.title('Pk/P')
plt.xlabel('density')
plt.ylabel('Pk/P')
plt.show()


