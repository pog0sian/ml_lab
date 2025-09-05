import numpy as np

# 2.7

arr = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
x = 3

idx = np.abs(arr - x).argmin()
closest = arr[idx]

print("Ближайшее к", x, "число в массиве:", closest)