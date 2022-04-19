# 1
import pandas as pd

row1 = [i for i in range(8)]
row2 = [0, 0, 0, 1, 1, 1, 1, 1]

res = pd.Series(row2, row1)

print(res)

# 2
import pandas as pd
import random

seed_value = int(input())
random.seed(seed_value)

data = [random.randint(50, 300) for i in range(5)]
res = pd.Series(data, ['01-04-2022', '02-04-2022', '03-04-2022', '04-04-2022', '05-04-2022'])

print(res.mean())

# 3
import pandas as pd
import random

seed_value = int(input())
random.seed(seed_value)

data = [random.randint(50, 300) for i in range(5)]
visits = pd.Series(data, ['01-04-2022', '02-04-2022', '03-04-2022', '04-04-2022', '05-04-2022'])
visHist = pd.DataFrame({'visits': visits,
                        'diff': visits - visits.mean()
                        })
                        
print(round(visHist.loc['02-04-2022', 'diff'], 1))