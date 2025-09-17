import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 1.2

x1 = [10, 20, 30]
y1 = [20, 40, 10]

x2 = [10, 20, 30]
y2 = [40, 10, 30]

plt.plot(x1, y1, color='blue', label='line1-width-3', linewidth=3)
plt.plot(x2, y2, color='red', label='line2-width-5', linewidth=5)

plt.tick_params(direction="in", top=True, right=True)

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(5))

plt.title('Two or more lines with different widths and colors with suitable legends')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.margins(0)

plt.legend()

plt.show()