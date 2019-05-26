import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/iris.data',sep=',',header=None)

df.columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid','class']

fig, axes = plt.subplots(1, 1, figsize=(5,5))

axes.scatter(df['sep_len'],df['pet_len'], s=2, label='Dimension', color='purple', marker='*')
axes.set_title('Sepal Length vs Petal Length')
axes.set_xlabel('Sepal Length (cm)')
axes.set_ylabel('Petal Length (cm)')
axes.legend()
plt.show()
plt.close()




