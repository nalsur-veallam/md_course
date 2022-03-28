import scipy.stats as stats
import pylab as plt
import numpy as np

maxwell = stats.maxwell
data = np.loadtxt('src/19900.xyz', skiprows = 1)
data = np.sqrt(data[:,4]**2 + data[:,5]**2 + data[:,6]**2)

params = maxwell.fit(data, floc=0)
print(params)
x = np.linspace(0, 25, 1000)

for i in range(0, 2000, 20):
	data = np.loadtxt(fname = 'src/'+ str(i) + '.xyz', skiprows = 1)
	data = np.sqrt(data[:,4]**2 + data[:,5]**2 + data[:,6]**2)

	fig, ax = plt.subplots()
	ax.twinx()
	ax = plt.hist(data, bins = 30, density=True, range = (0,8))
	ax1 = plt.plot(x, maxwell.pdf(x, *params), lw=3)
	plt.xlim(right = 8)
	fig.savefig('hists/' + str(i) + '.png')
