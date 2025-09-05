import numpy as np

# 2.9

arr = np.array(['Python', 'PHP', 'Java', 'C++'])
freq_p = np.array([s.count('P') for s in arr])
print("Частота 'P' в каждом элементе массива:", freq_p)