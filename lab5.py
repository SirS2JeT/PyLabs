import pandas as pd

df = pd.DataFrame({
    'Labels': list('AAABBCCA'),
    'Values': [0, 1, 2, 3, 4, 5, None, None],
    'Colors': ['red', 'blue', 'blue', 'green', 'red', 'black', 'green', 'red']
    })

#1
df_medians = df.groupby('Colors')['Values'].median()

print(df_medians, end='\n\n')

#2
df_refilled = df
df_refilled['Values'] = df.groupby('Colors')['Values'].transform(lambda x: x.fillna(x.median()))

print(df_refilled, end='\n\n')

#3
df_avrg = df_refilled.groupby('Colors')['Values'].mean()[df_refilled.groupby('Colors')['Values'].mean() > df_refilled['Values'].mean()]

print(df_avrg, end='\n\n')
print("Overall mean = " + str(df_refilled['Values'].mean()), end='\n\n')
print(df_refilled.groupby('Colors')['Values'].mean())
