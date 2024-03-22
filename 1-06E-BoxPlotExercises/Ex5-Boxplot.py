#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# create a DataFrame from the .csv file:
df_graph = pd.read_csv('../data/abalone.csv')

# take two random samples of different sizes:
sample_1 = np.random.choice(df_graph['rings'],200,replace=False)
sample_2 = np.random.choice(df_graph['rings'],200,replace=False)

# create a data variable with two Box plots:
data = [
    go.Box(
        y=sample_1,
        name='sample_1'
    ),
    go.Box(
        y=sample_2,
        name='sample_2'
    )
]

# add a layout
layout = go.Layout(
    title = 'Comparison of 2 samples extracted from same population'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='my_solution.html')