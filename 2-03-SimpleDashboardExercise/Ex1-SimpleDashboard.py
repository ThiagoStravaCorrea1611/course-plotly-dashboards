#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_core_components as dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
df_graph = pd.read_csv('../data/OldFaithful.csv')

fig1 = {
    'data': [
        go.Scatter(
            x = df_graph['X'],
            y = df_graph['Y'],
            mode = 'markers',
            marker = {
                'size': 12,
                'color': 'rgb(51,204,153)',
                'symbol': 'pentagon',
                'line': {'width': 2}
                }
        )
    ],
    'layout': go.Layout(
        title = 'Old Faithful Scatterplot',
        xaxis = {'title': 'Duration of eruption in minutes'},
        yaxis = {'title': 'Waiting time for next eruption in minutes'},
        hovermode='closest'
    )}

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    dcc.Graph(
        id='scatter1',
        figure=fig1
    )
])

# Add the server clause:
if __name__ == '__main__':
    app.run_server()

