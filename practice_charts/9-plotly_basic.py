import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_csv('data/iris.data',sep=',',header=None)
df.columns = ['sep_len', 'sep_wid', 'pet_len', 'pet_wid','class']


os.makedirs('plots', exist_ok=True)

fig = go.Figure()
fig.add_scatter(x=df['sep_len'],
                y=df['sep_wid'],
                mode='markers',
                marker={'color': df['sep_len'],
                        'opacity': 0.6,
                        'colorscale': 'Viridis'
                        })

plot(fig, filename='./plots/plotly-scatter.html', auto_open=False)



