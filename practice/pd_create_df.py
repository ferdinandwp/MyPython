import pandas as pd

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# Creating Dataframe from Lists
orders = pd.DataFrame(data=[['XB4Z34', 11, 25.50],
                            ['SZA1123', 34, 60],
                            ['P4FF2S', 2, 123.40],
                            ['PL34DS', 10, 1254.23],
                            ['PL34DS', 4, 12.4]],
                      columns=['Product', 'Qty', 'Price'])

#some basic info - how to get basic information of dataframe
#change column name if required
orders.columns = ['Product','Qty','Price']
pretty_print('orders',orders)

#convert to string
pretty_print('orders', orders.to_string())

#find total rows of dataframes
pretty_print("length of orders", len(orders))

#get first 3 rows
pretty_print("first_three", orders.head(3))

#columns
pretty_print("orders_columm",orders.columns)

#index
pretty_print("orders_index",orders.index)

#datatype
pretty_print("orders_dtype", orders.dtypes)

#shape
pretty_print("orders_shape", orders.shape)

#summarize info
pretty_print("orders_summary", orders.info())

#describe dataframe
pretty_print("orders_desc", orders.describe())


#extract values from dataframes
#sort by criteria
pretty_print('orders',orders)
pretty_print('by_price', orders.sort_values(by='Qty'))
pretty_print('by_price', orders.sort_values(by='Price'))

#count rows by criteria (grouping data)
pretty_print('by_Product', orders['Product'].value_counts())
pretty_print('by_Qty', orders['Qty'].value_counts())
pretty_print('by_Price', orders['Price'].value_counts())

#find null values
pretty_print('orders_null', orders.isnull())

#unique value count for each criteria
pretty_print('orders_unique', orders.nunique())
pretty_print('Orders_unique_Qty', orders['Qty'].unique())
