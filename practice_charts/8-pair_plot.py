import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

#Iris Pairplot
df = pd.read_csv('data/iris.data',sep=',',header=None)
df.columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid','class']

sns.pairplot(df, hue='class', diag_kind='hist')
# plt.savefig('plots/15-seaborn_pairplot/iris_pairplot.png')
plt.show()
plt.close()

