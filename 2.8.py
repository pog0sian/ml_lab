import numpy as np

arr1 = np.array(['Python', 'PHP'])
arr2 = np.array(['Java', 'C++'])

combined_arr = np.concatenate((arr1, arr2))
print("Объединенный массив:", combined_arr)