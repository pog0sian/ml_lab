import matplotlib.pyplot as plt

# 1.5

x1 = [2, 3, 5, 6, 8]
y1 = [1, 5, 10, 17, 20]

x2 = [3, 4, 6, 7, 9]
y2 = [2, 6, 11, 20, 22]

plt.plot(x1, y1, color='blue', linestyle='None', marker='*')
plt.plot(x2, y2, color='red', linestyle='None', marker='o')

plt.tick_params(direction="in", top=True, right=True)

plt.xlim(0, 10)
plt.ylim(0, 30)

plt.show()