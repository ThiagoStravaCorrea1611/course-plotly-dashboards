import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df_data_graph = pd.read_csv("..\\SourceData\\nst-est2017-alldata.csv")

df_data_graph = df_data_graph[df_data_graph["DIVISION"] == '1']

df_data_graph.set_index('NAME', inplace=True)

list_pop_cols = [col for col in df_data_graph.columns if col.startswith("POP")]

df_data_graph = df_data_graph[list_pop_cols]

data = [go.Scatter(
    x=df_data_graph.columns,
    y=df_data_graph.loc[name],
    mode='lines',
    name=name) for name in df_data_graph.index]

pyo.plot(data)