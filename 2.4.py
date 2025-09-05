import numpy as np

# 2.4

arr = np.array([1, 2, 3, 4, 5])
tiled_arr = np.tile(arr, 1)
print("1 повторение", tiled_arr)

tiled_arr = np.tile(arr, 2)
print("2 повторения", tiled_arr)

tiled_arr = np.tile(arr, 3)
print("3 повторения", tiled_arr)

