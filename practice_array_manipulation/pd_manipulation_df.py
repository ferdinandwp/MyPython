import numpy as np
import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


titanic = pd.read_csv(filepath_or_buffer='titanic/train.csv',
                      sep=',',
                      header=0)

# Getting DataFrames information
pretty_print("titanic dataframe", titanic.to_string())
pretty_print("titanic columns", titanic.columns)

#drop some rows
pretty_print("dropping the row with index 1", titanic.drop(1))

#drop entire column
pretty_print('drop a column', titanic.drop(('Embarked'), axis = 1))



