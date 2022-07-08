import random
import numpy as np
import pylab as plt

def integral(n):
    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0

    count = 0
    for i in range(0, n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        # x * x> y означает, что точка находится ниже кривой. Рассчитанное интегральное значение представляет собой отношение площади под кривой к площади квадрата.
        if np.sqrt(1-x**2) > y:
            count += 1

    integral_value = count / float(n)
    return integral_value
    
integr = []
for i in range(1, 10000):
    integr.append(integral(10*i) - np.pi/4)
    if abs(integr[i-1]) < 0.0001:
        print(i*10)
    
fig, ax = plt.subplots(figsize=(15,12))

plt.plot(integr, lw=3)
plt.grid()
plt.legend()
plt.xlabel('number steps / 10', fontsize=20)
plt.ylabel('error', fontsize=20)
plt.title('Integration error by the Monte-Carlo method on the number of steps', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
fig.savefig('mc2.pdf')
#~10000
