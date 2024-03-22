#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df_graph = pd.read_csv('../data/abalone.csv')

# create a data variable:
data = [go.Histogram(
    x=df_graph['length'],
    xbins=dict(start=0,end=1,size=0.02),
)]

# add a layout
layout = go.Layout(
    title="Histogram for Lengths"
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='my+solution.html')