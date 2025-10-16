import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [
    ["Вжик", "Zipper the Fly", "fly", "0.7"],
    ["Гайка", "Gadget Hackwrench", "mouse", None],
    ["Дейл", "Dale", "chipmunk", "1"],
    ["Рокфор", "Monterey Jack", "mouse", "0.8"],
    ["Чип", "Chip", "chipmunk", "0.2"]]

# 2.1

df = pd.DataFrame(data, columns=['ru_name', 'en_name', 'class', 'cheer'])
df['cheer'] = pd.to_numeric(df['cheer'], errors='coerce')

print(df.dtypes)

# 2.2

print(len(df))

# 2.3

print(df['cheer'].notnull().sum())

# 2.4

print(df['en_name'][2])

# 2.5

df1 = df.drop(columns=['cheer'])[2:]

print(df1)

# 2.6

print(df)

# 2.7

df['logcheer'] = np.log(df['cheer'])

# 2.8

x = df['class'].value_counts().index
y = df['class'].value_counts().values

plt.bar(x, y)
plt.title('Частота встречаемости классов')
plt.xlabel('Класс')
plt.ylabel('Частота')
plt.show()

