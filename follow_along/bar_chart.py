import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df_data_graph = pd.read_csv("..\\Data\\2018WinterOlympics.csv")

trace1 = go.Bar(
            x=df_data_graph["NOC"],
            y=df_data_graph["Gold"],
            name="Gold",
            marker={"color": "#FFD700"})

trace2 = go.Bar(
            x=df_data_graph["NOC"],
            y=df_data_graph["Silver"],
            name="Silve",
            marker={"color": "#9EA0A1"})

trace3 = go.Bar(
            x=df_data_graph["NOC"],
            y=df_data_graph["Bronze"],
            name="Bronze",
            marker={"color": "#CD7F32"})

data = [trace1, trace2, trace3]

layout = go.Layout(
    title='Medals',
    barmode='stack')

fig = go.Figure(
    data=data,
    layout=layout
)

pyo.plot(
    fig,
    filename = 'barchart_2.html')
