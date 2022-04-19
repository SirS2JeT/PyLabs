# 1
import pandas as pd
import random

seed_value = int(input())
random.seed(seed_value)

df = pd.DataFrame({'ID': [10,11,12,13,14,15,16], 
                  'Type': ['A','B','C','A','C','D','A'],
                  'Task': ['First','Second','First','Second','Third','First','Fifth'],
                  'Color': ['blue','red','blue','black','red','red','red'],
                  'Link': [123,123,123,523,523,523,765],
                  'Price': [random.randint(100, 1000) for _ in range(7)],
                  'Volume': [random.uniform(10, 100) for _ in range(7)],
                  })
                  
df_med = df.groupby('Type')['Price'].median()

print(round(df_med.loc['D']))

# 2
import pandas as pd
import random

seed_value = int(input())
random.seed(seed_value)

df = pd.DataFrame({'ID': [10,11,12,13,14,15,16], 
                  'Type': ['A','B','C','A','C','D','A'],
                  'Task': ['First','Second','First','Second','Third','First','Fifth'],
                  'Color': ['blue','red','blue','black','red','red','red'],
                  'Link': [123,123,123,523,523,523,765],
                  'Price': [random.randint(100, 1000) for _ in range(7)],
                  'Volume': [random.uniform(10, 100) for _ in range(7)],
                  })
                  
df_sum = df.groupby(['Task', 'Color'])['Volume'].sum()

print(round(df_sum['First', 'blue'], 2))

# 3
import pandas as pd
import random

seed_value = int(input())
random.seed(seed_value)

df = pd.DataFrame({'ID': [10,11,12,13,14,15,16], 
                  'Type': ['A','B','C','A','C','D','A'],
                  'Task': ['First','Second','First','Second','Third','First','Fifth'],
                  'Color': ['blue','red','blue','black','red','red','red'],
                  'Link': [123,123,123,523,523,523,765],
                  'Price': [random.randint(100, 1000) for _ in range(7)],
                  'Volume': [random.uniform(10, 100) for _ in range(7)],
                  })
                  
df_mean = df.groupby('Link')['Volume'].mean() > 40

print(df_mean.loc[df_mean].index.to_list())