import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
widths = [0.2, 0.3, 0.5, 0.6, 0.3, 0.4]

bars = plt.bar(x, y, color="blue", width=widths, align='edge')

plt.title("Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago")

plt.xlim(0, 6)
plt.ylim(0, 25)

plt.grid(which='major', color='red', linestyle='-', linewidth=0.7)
plt.grid(which='minor', color='black', linestyle=':', linewidth=0.3)

plt.minorticks_on()
plt.tick_params(axis='y', which='minor', length=4)

plt.ylabel("Popularity")
plt.xlabel("Languages")

plt.show()