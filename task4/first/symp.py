import sympy
import numpy as np
import pylab as plt
 
x = sympy.Symbol('x')
 
f_x = (1 - x**2)**(1/2)
 
 
def sympson(left, right, n, function):
    h = (right - left) / (2 * n)
 
    tmp_sum = float(function.subs({x: left})) +\
        float(function.subs({x: right}))
 
    for step in range(1, 2 * n):
        if step % 2 != 0:
            tmp_sum += 4 * float(function.subs({x: left + step * h}))
        else:
            tmp_sum += 2 * float(function.subs({x: left + step * h}))
 
    return tmp_sum * h / 3
 


integr = []
for i in range(1, 100):
    integr.append(sympson(0, 1, 10*i, f_x) - np.pi/4)
    if abs(integr[i-1]) < 0.00001:
        print(i*10)
    
fig, ax = plt.subplots(figsize=(15,12))

plt.plot(integr, lw=3)
plt.grid()
plt.legend()
plt.xlabel('number steps / 10', fontsize=20)
plt.ylabel('error', fontsize=20)
plt.title('Integration error by the Simpson method on the number of steps', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
fig.savefig('symp.pdf')
#Уже на 60ом шаге
