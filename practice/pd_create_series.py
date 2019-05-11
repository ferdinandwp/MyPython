import numpy as np
import pandas as pd

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n')

#create data series using pandas
orders = pd.Series(data=[300.50, 60, 123.40, 60, np.nan],
                    index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'])
pretty_print("initial dataset",orders)

#convert to string
pretty_print('to_string', orders.to_string())

#get first 2 rows
pretty_print('first_two_rows',orders.head(2))

#describe index
pretty_print('order_index',orders.index)

#describe data type
pretty_print('order_datatype',orders.dtype)

#describe shape
pretty_print('order_shape',orders.shape)

#summarize series
pretty_print('orders_with_desc',orders.describe())

#sort values
pretty_print('orders_sorted',orders.sort_values())

#count data categories
pretty_print('orders_count', orders.value_counts())

#check for null value
pretty_print('orders_null_data',orders.isnull())






