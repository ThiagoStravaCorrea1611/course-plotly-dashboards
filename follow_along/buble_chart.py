import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df_data_graph = pd.read_csv("..\\Data\\mpg.csv")
df_data_graph = df_data_graph[df_data_graph.horsepower != "?"]
df_data_graph['horsepower']=pd.to_numeric(df_data_graph['horsepower'])
df_data_graph.sort_values(by=['horsepower'], inplace=True)

data = [go.Scatter(
    x=df_data_graph['horsepower'],
    y=df_data_graph['mpg'],
    text=df_data_graph['name'],
    mode='markers',
    marker=dict(
        size=df_data_graph['weight']/100,
        color=df_data_graph['cylinders'],
        showscale=True))]

layout = go.Layout(title="Bubbble Chart")

fig = go.Figure(
    data=data,
    layout=layout)

pyo.plot(
    fig,
    filename = 'bubble.html')