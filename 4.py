import pandas as pd

# 1.1

polit = pd.read_csv('polit.csv', decimal=',')
polit = polit.dropna(how='all')

# 1.2

print(polit[polit['fh09'] > 5])

# 1.3

print(polit[(polit['afri'] == 1) & (polit['fparl08'] > 30)])

# 1.4

print(polit[((polit['afri'] == 1) | (polit['lati'] == 1)) & (polit['polity09'] >= 8)])

# 1.5

polit['corr_round'] = polit['corr0509'].round(2)
print(polit[['ctry', 'corr_round', 'corr0509']])

# 1.6

def map_fh_status(x):
    if x <= 2.5:
        return 'free'
    elif x <= 5.0:
        return 'partly free'
    else:
        return 'not free'

polit['fh_status'] = polit['fh09'].apply(map_fh_status)
print(polit[['ctry', 'fh09', 'fh_status']])

# 1.7

gini_stats = polit.groupby('fh_status')['gini'].agg(min='min', mean='mean', max='max').reset_index()
print(gini_stats)

# 1.8

for name, group in polit.groupby('fh_status'):
    fname = f"polit_{name.replace(' ', '_')}.csv"
    group.to_csv(fname, index=False)