import matplotlib.pyplot as plt
import numpy as np

# 3

x = np.linspace(-3, 5, 400)
y = x * x - x - 6

plt.plot(x, y, label='y = x^2 - x - 6')
plt.axhline(0, color='black', linewidth=0.8)  # ось x
plt.axvline(0, color='grey', linewidth=0.5, linestyle='--')  # ось y
plt.title('График функции y = x^2 - x - 6')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()