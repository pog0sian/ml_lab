import matplotlib.pyplot as plt

x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]

plt.plot(x, y, color='red', linestyle='dashdot')
plt.plot(x, y, color='blue', linestyle='None', marker='o')

plt.tick_params(direction="in", top=True, right=True)

plt.xlim(1, 8)
plt.ylim(1, 8)

plt.title('Display marker')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.margins(0)

plt.show()