import pandas as pd

# 1.1

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# 1.2

print(s['d'])

# 1.3

print(s[1])

# 1.4

s['f'] = 6

# 1.5

print(s[2:5])

# 1.6

df = pd.DataFrame([[1, 2], [5, 3], [3.7, 4.8]], columns=['col1', 'col2'])

# 1.7

print(df['col1'][2])

# 1.8

df.loc[1, 'col2'] = 9

# 1.9

print(df.iloc[0:1, 0:2])

# 1.10

df['col3'] = df['col1'] * df['col2']