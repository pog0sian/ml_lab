import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

x = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
y = [772.5, 776.42, 776.47, 776.85, 775.1]

plt.plot(x, y, color='red', marker='o')

ax = plt.gca()
ax.yaxis.set_major_locator(MultipleLocator(0.5))

plt.xlim('2016-10-03', '2016-10-07')
plt.ylim(772.5, 777.0)

plt.grid(which='major', color='red', linestyle='-', linewidth=0.7)
plt.grid(which='minor', color='black', linestyle=':', linewidth=0.5)

plt.minorticks_on()
plt.tick_params(axis='y', which='minor', length=4)

plt.title('Closing stock value of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Value')

plt.show()