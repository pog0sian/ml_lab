import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 1.3

x1 = [10, 20, 30]
y1 = [20, 40, 10]

x2 = [10, 20, 30]
y2 = [40, 10, 30]

plt.plot(x1, y1, color='blue', label='line1-dotted', linestyle='dotted')
plt.plot(x2, y2, color='red', label='line2-dashed', linestyle='dashed')

plt.tick_params(direction="in", top=True, right=True)

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(5))

plt.title('Plot with two or more lines with different styles')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.margins(0)

plt.legend()

plt.show()