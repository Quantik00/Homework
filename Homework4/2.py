import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10, 5))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

values1 = np.random.laplace(0, 1000, 100000)
ax1.hist(values1, color='m', bins=200)
ax1.grid() 

values2 = np.random.normal(0, 5, 1000)
ax2.hist(values2, bins = 200)
ax2.grid()

plt.show()