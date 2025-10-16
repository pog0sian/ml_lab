import pandas as pd

# 1.1

df = pd.read_csv('vgsales.csv')
print(df['Platform'].unique())

# 1.2

meta = pd.read_csv('metacritic_games.csv')

df_copy = df.copy()
df_copy = df_copy.merge(
    meta[['name', 'rating']],
    left_on='Name',
    right_on='name',
)

df_copy.rename(columns={'rating': 'metacritic_rating'}, inplace=True)
print(df_copy)

# 1.3

filtered_df = df_copy[(df_copy['metacritic_rating'] == 'M') & (df_copy['Year'] >= 2012)]
print(filtered_df[['Name', 'metacritic_rating', 'Year']])

# 1.4

print(filtered_df.describe())

# 1.5

def has_3_unique_vowels(text):
    if pd.isna(text):
        return False
    vowels = set('aeiou')
    text_lower = str(text).lower()
    unique_vowels = {char for char in text_lower if char in vowels}
    return len(unique_vowels) >= 3

genre_counts = df_copy['Genre'].value_counts()

print("Жанры с количеством игр (содержат ≥ 3 различных гласных):")
for genre, count in genre_counts.items():
    if has_3_unique_vowels(genre):
        print(f"{genre} - {count}")