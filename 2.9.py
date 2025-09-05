import numpy as np

arr = np.array(['Python', 'PHP', 'Java', 'C++'])
freq_p = np.array([s.count('P') for s in arr])
print("Частота 'P' в каждом элементе массива:", freq_p)