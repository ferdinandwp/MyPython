import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('data/iris.data',sep=',',header=None)
df.columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid','class']

plt.style.use("ggplot")

sns.set()

#sort df
sorted_df = df.sort_values('sep_len')

sns.lineplot('sep_len','sep_wid', data=sorted_df)
sns.lineplot('sep_len','pet_wid', data=sorted_df)

# sns.scatterplot('sep_len','sep_wid',data=df)
plt.legend()

plt.show()
plt.close()
