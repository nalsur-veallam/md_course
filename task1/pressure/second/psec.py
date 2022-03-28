import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output



data = np.loadtxt('0.txt', skiprows = 11)
p = data[:,7]
P0 = np.mean(p[len(p) - 100 : len(p)])

rc = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0]
pcor = [-1.39626, -0.51814, -0.15500, -0.06544, -0.03351, -0.01939, -0.00818, -0.00419, -0.00242]

P = []
Pc = []

for i in rc:
	data = np.loadtxt(str(int(i)) + '.txt', skiprows = 11)
	p = data[:,7]
	P.append(np.mean(p[len(p) - 100 : len(p)]) - P0)

x = np.linspace(0.89, 12, 100)


plt.scatter(rc, P)
plt.plot(x, 16.0/3.0*np.pi*0.25*(2.0/3.0/(x**9)-1/(x**3)))
plt.title('pcor from rcut')
plt.xlabel('rcut')
plt.ylabel('pcor')
plt.show()
