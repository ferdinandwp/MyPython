import pandas as pd


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

#import dataframe
titanic = pd.read_csv(filepath_or_buffer='titanic/train.csv',
                        sep=',',
                        header=0)

#show data & columns
pretty_print('titanic',titanic.to_string())
pretty_print('titanic_df:',titanic.columns) #show all columns

#choose selected column(s)
pretty_print('check_column_type', titanic['Name'])
pretty_print('check_column_type', titanic[['Name', 'Age', 'Sex']])
pretty_print('check_column_type', titanic[['Name', 'Age', 'Sex']].head(5))

#perform column operations
pretty_print('sum_fares_and_ages', titanic['Fare'] + titanic['Age'])

#select df using loc function
pretty_print('first_row',titanic.loc[1]) #describe specific row

#select using iloc index
pretty_print('first_three_rows', titanic.iloc[[1,2,3,4,5],[3,4]])

#select rows & columns by index
pretty_print('selected', titanic.iloc[37:49, 3:6])

#select rows by criteria
pretty_print('condition', titanic[titanic['Age'] > 30])
pretty_print('multiple_criteria', 
                             titanic[(titanic['Age'] > 30) & (titanic['Fare'] > 30) & (titanic['Survived'] == 1)])


#correlation
pretty_print('Correlation', titanic.corr().to_string())



