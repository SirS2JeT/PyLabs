import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-ticks')
plt.rcParams.update({'figure.figsize': (6, 4), 'font.size': 14})

df = pd.read_csv('insurance.csv')

sns.scatterplot(x='bmi', y='charges', data=df, hue='smoker');


plt.show()

