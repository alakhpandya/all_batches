import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 13)
y = np.random.randint(low=20, high=200, size=12)
print("x =", x)
print("y =", y)

plt.bar(x, y)
plt.show()