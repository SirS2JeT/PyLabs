import pandas as pd

df = pd.read_csv('IMDB-Movie-Data.csv')

#1
df_duples = df[df['Title'].duplicated()]

print(df_duples['Title'], end='\n\n')

#2
df_SciFi = df.loc[(df['Year'] == 2016) & (df['Genre'].str.contains('Sci-Fi')), 'Title'].count()

print(df_SciFi)

#3
df_border = df[(df['Runtime (Minutes)'] == df['Runtime (Minutes)'].max()) | (df['Runtime (Minutes)'] == df['Runtime (Minutes)'].min())]

print(df_border[['Runtime (Minutes)', 'Title', 'Director']])

#4
df_oscar = df[df['Actors'].str.contains('Leonardo DiCaprio')].sort_values(by='Rating', ascending=False)

print(df_oscar[['Rating', 'Title']])
