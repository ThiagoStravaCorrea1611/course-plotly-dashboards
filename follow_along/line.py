import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace_0 = go.Scatter(
    x=x_values,
    y=y_values+5,
    mode='markers',
    name='markers')

trace_1 = go.Scatter(
    x=x_values,
    y=y_values,
    mode='lines',
    name='lines')

trace_2 = go.Scatter(
    x=x_values,
    y=y_values-5,
    mode='lines+markers',
    name='lines+markers')

data = [trace_0, trace_1, trace_2]

layout = go.Layout(
    title='Line Charts')

fig = go.Figure(
    data=data,
    layout=layout)

pyo.plot(fig)
