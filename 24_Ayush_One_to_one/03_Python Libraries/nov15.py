import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2.1, 0.25)
y = np.random.randint(low=0, high=15, size=9)

plt.plot(x, y)
plt.show()