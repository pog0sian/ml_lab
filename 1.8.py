import numpy as np

# 1.8

arr = np.zeros((5, 5), dtype=int)
np.fill_diagonal(arr, np.arange(1, 6))

print("Массив с диагональю от 1 до 5:\n", arr)