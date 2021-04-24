import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1,1,1000)

fx1 = np.sqrt(abs(x)) + np.sqrt(1-x**2)
fx2 = np.sqrt(abs(x)) - np.sqrt(1-x**2)

plt.plot(fx1, color='r')
plt.plot(fx2, color='r')
plt.show()