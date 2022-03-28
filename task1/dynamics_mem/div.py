import numpy as np
import pylab as plt



data = np.loadtxt('5.txt')


V = data[:,2]
R = data[:,1]

fig, ax = plt.subplots()
ax = plt.plot(range(len(R)), R)
plt.title('Невязка r')
plt.ylabel('невязка')
plt.xlabel('t')
fig.savefig('r_div.png')

fig, ax = plt.subplots()
ax = plt.plot(range(len(V)), V)
plt.title('Невязка v')
plt.ylabel('невязка')
plt.xlabel('t')
plt.show()
fig.savefig('v_div.png')
