import numpy as np

# 2.6

arr = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
k = 3

smallest_k = np.partition(arr, k)[:k]
print("k наименьших элементов:", smallest_k)