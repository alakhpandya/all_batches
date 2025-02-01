import numpy as np
import matplotlib.pyplot as plt

y = np.random.randint(low=0, high=20, size=9)
x = ["Rank", "Name", "Numpy", "Genre", "Python", "Nihar", "Mithil", "Neel", "Gunjan"]
plt.bar(x, y)