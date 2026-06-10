import numpy as np
import matplotlib.pyplot as plt

# x = 4
# print(x + 5)
# print(x.__add__(15))

# a = np.array([1,2,3])
# print(a.__add__(5))
# print(type(a))

x = np.arange(1, 13)
y = np.random.randint(20, 200, 12)
print("x =", x)
print("y =", y)

plt.bar(x, y)
plt.show()