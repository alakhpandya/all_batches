import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1, 13)
y = np.random.randint(low=50, high=200, size=12)
# print("x =", x)
# print("y =", y)

plt.bar(x, y)
plt.show()