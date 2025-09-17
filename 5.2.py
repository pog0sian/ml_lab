import matplotlib.pyplot as plt

# 5.2

x = [22, 17.7, 8.9, 8, 7.8, 6.8]
y = ["Java", "Python", "PHP", "JS", "C#", "C++"]


plt.barh(y, x, color='green', height=0.6, align='edge')

plt.xlabel('Popularity')
plt.ylabel('Languages')

plt.title('Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago')
plt.xlim(0, 25)
plt.ylim(0, 6)

plt.grid(which='major', color='red', linestyle='-', linewidth=0.7)
plt.grid(which='minor', color='black', linestyle=':', linewidth=0.3)

plt.minorticks_on()
plt.tick_params(axis='y', which='minor', length=4)

plt.show()