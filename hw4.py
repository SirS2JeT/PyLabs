# 1
import pandas as pd
import random

seed_value = int(input())
random.seed(seed_value)

df = pd.DataFrame({
    'Col1': [random.uniform(0, 10) for _ in range(5)],
    'Col2': [random.uniform(0, 10) for _ in range(5)],
    'Col3': [random.uniform(0, 10) for _ in range(5)]
})
# заменим случайно выбранные элементы значением None
for _ in range(8):
    null_ind = random.randint(0, 4), random.randint(0, 2)
    df.iloc[null_ind[0], null_ind[1]] = None

df = df.transform(lambda x: x.fillna(x.mean()))
df_sum = df['Col1'].sum() + df['Col2'].sum() + df['Col3'].sum()

print(round(df_sum, 2))
# print(df)

#2
import pandas as pd
import random

seed_value = int(input())
random.seed(seed_value)

df = pd.DataFrame({
    'Col1': [random.uniform(0, 10) for _ in range(5)],
    'Col2': [random.uniform(0, 10) for _ in range(5)],
    'Col3': [random.uniform(0, 10) for _ in range(5)],
    'Col4': list('AABCD')
})
# заменим случайно выбранные элементы значением None
for _ in range(5):
    null_ind = random.randint(0, 4), random.randint(0, 2)
    df.iloc[null_ind[0], null_ind[1]] = None

# Группировка по Col4 не имеет смысла и ведет к получению неверных значений
df_non = df.dropna().count()


print(df_non['Col1'])S