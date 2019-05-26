import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/iris.data',sep=',',header=None)
df.columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid','class']

os.makedirs('plots',exist_ok=True)

for col1_idx, column1 in enumerate(df.columns):
    for col2_idx, column2 in enumerate(df.columns):
        if col1_idx < col2_idx:
            fig, axes = plt.subplots(1, 1, figsize=(5,5))
            axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='black', marker='x')
            axes.set_title = (f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/data_exploration_{column1}_vs_{column2}.png',dpi=300)
            plt.clf()
plt.close()








