import numpy as np

arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([10, 30, 40])

common_elements = np.intersect1d(arr1, arr2)
print("Общие элементы в arr1 и arr2:", common_elements)