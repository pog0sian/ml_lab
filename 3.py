import numpy as np

print("Введите коэффициенты a11, a12 и b1 для уравнения a11*x + a12*y = b1:")
a11, a12, b1 = map(float, input().split())

print("Введите коэффициенты a21, a22 и b2 для уравнения a21*x + a22*y = b2:")
a21, a22, b2 = map(float, input().split())

A = np.array([[a11, a12], [a21, a22]])
B = np.array([b1, b2])

det = np.linalg.det(A)

if det == 0:
    print("Система уравнений не имеет решения или имеет бесконечное множество решений (определитель равен 0).")
else:
    solution = np.linalg.solve(A, B)
    print(f"Решение системы уравнений: x = {solution[0]}, y = {solution[1]}")