import pandas as pd

# 1.1

df = pd.read_csv('la-crimes-sample.csv')

# 1.2

print(df.shape[0], df.shape[1])

# 1.3

print(df.columns)

# 1.4

print(df.nunique())

# 1.5

print(df.isnull().sum().sum())

# 1.6

f = (df['Victim Sex'] == 'F').sum()
m = (df['Victim Sex'] == 'M').sum()
if f > m:
    print('Жертв среди женщин больше, чем среди мужчин')
else:
    print('Жертв среди мужчин больше, чем среди женщин')