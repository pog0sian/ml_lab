import numpy as np

# 1.1

arr = np.array([1, 7, 13, 105])

print("Размер памяти (байт):", arr.nbytes)

np.savetxt('array.txt', arr, fmt='%d')
np.save('array.npy', arr)

arr_txt = np.loadtxt('array.txt', dtype=int)
print("Массив из текстового файла:", arr_txt)

arr_npy = np.load('array.npy')
print("Массив из бинарного файла:", arr_npy)