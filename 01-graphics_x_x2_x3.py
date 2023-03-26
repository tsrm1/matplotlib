
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
# Plot some data on the (implicit) axes.
plt.plot(x, x, label='linear', marker='x')
plt.plot(x, x**2, label='quadratic', marker='o')  # etc.
plt.plot(x, x**3, label='cubic', marker='*')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("Simple Plot")
plt.legend()

plt.show()
# plt.savefig("01-graphics_x_x2_x3.png", dpi=227)
