import pandas as pd
import random

random.seed(33)

row = [random.randint(-15, -10) for i in range(5)]

temper = pd.Series(row, ['01-02-2022', '03-02-2022', '05-02-2022', '07-02-2022', '09-02-2022'])

print(temper.mean())

dailyTemp = pd.DataFrame({'temp_day': temper, 'temp_night': temper*1.5, 'temp_diff': temper-temper*1.5})

print(dailyTemp, end='\n\n')
print(dailyTemp.loc[['07-02-2022'], ['temp_diff']])
