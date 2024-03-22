#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df_data_graph = pd.read_csv("..\\Data\\mpg.csv")
df_data_graph = df_data_graph[df_data_graph.horsepower != "?"]
df_data_graph['horsepower']=pd.to_numeric(df_data_graph['horsepower'])
df_data_graph.sort_values(by=['acceleration'], inplace=True)

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(
    x=df_data_graph['acceleration'],
    y=df_data_graph['displacement'],
    text=df_data_graph['name'],
    mode='markers',
    marker=dict(
        size=df_data_graph['mpg'],
        color=df_data_graph['origin'],
        showscale=True))]

layout = go.Layout(title="Bubbble Chart")

fig = go.Figure(
    data=data,
    layout=layout)

pyo.plot(
    fig,
    filename = 'bubble.html')







# create a layout with a title and axis labels







# create a fig from data & layout, and plot the fig
