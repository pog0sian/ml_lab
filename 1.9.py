import numpy as np

arr = np.indices((4, 4)).sum(axis=0) % 2
np.fill_diagonal(arr, 0)

print("Шахматный узор 4x4:\n", arr)