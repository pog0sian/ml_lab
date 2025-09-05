import numpy as np

coeffs_a = [1, -4, 7]
roots_a = np.roots(coeffs_a)
print("Корни уравнения x^2 - 4x + 7:", roots_a)

coeffs_b = [1, -11, 9, 11, -10]
roots_b = np.roots(coeffs_b)
print("Корни уравнения x^4 - 11x^3 + 9x^2 + 11x - 10:", roots_b)