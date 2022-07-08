import numpy as np
import pylab as plt

spin1 = [-0.99847, 0.86729, -0.00017, -0.00054, 0.00576]
en1 = [-1.99609, -1.74122, -0.81896, -0.55622, -0.43209]
spin2 = [-0.99827, -0.90915, -0.00247, 0.00281, 0.00160]
en2 =[-1.99568, -1.74271, -0.81748, -0.55921, -0.42892]
spin3 = [0.99854, 0.57220, 0.00122, 0.00422, -0.00182]
en3 = [-1.99603, -1.74411, -0.82000, -0.56158, -0.42791]
spin = [-0.96888, 0.95542, -0.93647, -0.47646, 0.09416, 0.02595]
en = [-1.89564, -1.85625, -1.80626, -1.66090, -1.54720, -1.39561]
x = [1,2,3,4,5]

fig, ax = plt.subplots(figsize=(15,12))

ax.scatter(x, spin1, color='blue', label='seed #1',lw=3)
ax.scatter(x, spin2, color='green', label='seed #2',lw=3)
ax.scatter(x, spin3, color='red', label='seed #3',lw=3)
ax.scatter([1.7, 1.8, 1.9, 2.1, 2.2, 2.3], spin, color='green',lw=3)
plt.grid()
plt.legend()
plt.xlabel('Temperature', fontsize=20)
plt.ylabel('Spin', fontsize=20)
plt.title('Spin from Temperature', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
fig.savefig('spin.pdf')

fig, ax = plt.subplots(figsize=(15,12))

ax.scatter(x, en1, color='blue', label='seed #1',lw=3)
ax.scatter(x, en2, color='green', label='seed #2',lw=3)
ax.scatter(x, en3, color='red', label='seed #3',lw=3)
ax.scatter([1.7, 1.8, 1.9, 2.1, 2.2, 2.3], en, color='green',lw=3)
plt.grid()
plt.legend()
plt.xlabel('Temperature', fontsize=20)
plt.ylabel('Energy', fontsize=20)
plt.title('Energy from Temperature', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
fig.savefig('energy.pdf')
