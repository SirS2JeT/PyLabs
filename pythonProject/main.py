import pandas as pd

left_data = {'col1': ['x', 'y', 'z'],
             'col2': [0, 1, 2]
             }
right_data = {'col1': ['a', 'b', 'c'],
              'col3': [6, 7, 8]
              }
left = pd.DataFrame(left_data, index=[0, 1, 2])
right = pd.DataFrame(right_data, index=[1, 2, 3])

#1

df_concat0 = pd.concat([left, right]).reset_index(drop=True)

print(df_concat0, end='\n\n')

df_concat1 = pd.concat([df_concat0, left, right], axis=1)

print(df_concat1, end='\n\n')


#2


#3
# датафрейм с покупателями
customers = {'CustomerID': [1, 2, 3],
              'Name': ['Bob', 'Rob', 'Kob'],
              'Address': ['Address1', 'Address2', 'Address3']
             }
customers = pd.DataFrame(customers)

# датафрейм с заказами
orders = {'OrderID': [1001, 1002, 1003, 1004],
          'CustomerID': [1, 2, 1, 5]
          }
orders = pd.DataFrame(orders)


