import numpy as np

arr = np.array([10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 50])
unique, counts = np.unique(arr, return_counts=True)

print("Уникальные элементы:", unique)
print("Частота каждого элемента:", counts)
