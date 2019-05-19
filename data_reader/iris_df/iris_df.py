#read iris data
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
iris_df = pd.read_csv(filepath_or_buffer='iris.data',sep=',')

#add column to the dataframe
iris_df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid','class']

#change column name
modified_iris_df = iris_df.rename(columns={'sepal_len':'sep_len','sepal_wid':'sep_wid','petal_len':'pet_len','petal_wid':'pet_wid'})

#print dataset
print(modified_iris_df.to_string())
print()

#summarize dataset 
print(modified_iris_df.describe())
print()

print(modified_iris_df.dtypes)
print()
#add column
#remove column
#column operations
#data cleansing



