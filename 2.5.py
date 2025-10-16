import numpy as np

# 2.5

arr = np.array([200., 300., np.nan, np.nan, np.nan, 700.])
clean_arr = arr[~np.isnan(arr)]

print("Массив без NaN значений:", clean_arr)