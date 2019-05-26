import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/iris.data',sep=',',header=None)
df.columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid','class']

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.grid(axis='y', alpha=0.5)
axes.scatter(df['sep_len'], df['sep_wid'])
axes.scatter(df['pet_len'], df['pet_wid'])
axes.scatter(df['sep_len'], df['pet_len'])
axes.set_title(f'Dimension Comparison')
axes.legend()

plt.show()
plt.close()




