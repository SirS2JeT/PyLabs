import pandas as pd

df = pd.read_csv('IMDB-Movie-Data.csv')

#1
df_revenue = df.groupby('Director')['Revenue (Millions)'].sum()

print(df_revenue, end='\n\n')

#2.1
df_rewieves = df.groupby(['Year', 'Director']).agg(
    SumVotes=('Votes', 'sum'),
    AvgMetascore=('Metascore', 'mean')
)

print(df_rewieves, end='\n\n')

#2.2
pt_rewieves = pd.pivot_table(data=df,
                             index=['Year', 'Director'],
                             values=['Votes', 'Metascore'],
                             aggfunc={'Votes': 'sum',
                                      'Metascore': 'mean'}
                             )
print(pt_rewieves, end='\n\n')

#3
df_SciFi_Yearly = df[df['Genre'].str.contains('Sci-Fi')].groupby('Year').count().sort_values('Title', ascending=True)

print(df_SciFi_Yearly['Title'])
