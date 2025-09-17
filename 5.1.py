import matplotlib.pyplot as plt

# 5.1

x = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(x, y, color='blue', width=0.8, align='edge')

plt.xlabel('Languages')
plt.ylabel('Popularity')

plt.title('PopularitY of Programming Languages\nWorldwide, Oct 2017 compared to a year ago')

plt.xlim(0, 6)
plt.ylim(0, 25)

plt.grid(which='major', color='red', linestyle='-', linewidth=0.7)
plt.grid(which='minor', color='black', linestyle=':', linewidth=0.5)

plt.minorticks_on()
plt.tick_params(axis='y', which='minor', length=4)


plt.show()