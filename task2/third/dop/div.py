import numpy as np
import pylab as plt

dt = 50*0.1

data = np.loadtxt('5.txt')


V = data[:,2]
R = data[:,1]

fig, ax = plt.subplots()
ax = plt.plot(range(len(R)), R)
plt.title('Невязка r')
plt.ylabel('невязка')
plt.xlabel('t')
fig.savefig('r_div.png')
plt.show()

D = -1/12*(R[40]-R[90])/dt
print(D)
