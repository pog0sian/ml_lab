import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

bars = plt.bar(x, y, color="blue", width=0.8, align='edge')

plt.title("Popularity of Programming Languages\nWorldwide, Oct 2017 compared to a year ago")

plt.xlim(0, 6)
plt.ylim(0, 25)

plt.grid(which='major', color='red', linestyle='-', linewidth=0.7)
plt.grid(which='minor', color='black', linestyle=':', linewidth=0.3)

plt.minorticks_on()
plt.tick_params(axis='y', which='minor', length=4)

plt.ylabel("Popularity")
plt.xlabel("Languages")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.5,
        f'{bar.get_height()}',
        ha='center',
        va='bottom'
    )

plt.show()