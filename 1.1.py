import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 1.1

x = range(1, 50)
y = [3 * i for i in x]

plt.plot(x, y, color='blue')

plt.tick_params(direction="in", top=True, right=True)

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_locator(MultipleLocator(20))

plt.xlim(0, 50)
plt.ylim(0, 160)

plt.title('Draw a line.')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.margins(0.05)

plt.show()