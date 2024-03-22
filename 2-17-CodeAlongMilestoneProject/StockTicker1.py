#######
# First Milestone Project: Develop a Stock Ticker
# dashboard that either allows the user to enter
# a ticker symbol into an input box, or to select
# item(s) from a dropdown list, and uses pandas_datareader
# to look up and display stock data on a graph.
######

# DEVELOP THE GRAPH LAYOUT FIRST, AND LEAVE THE CALLBACK FOR THE NEXT PHASE
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd

app = dash.Dash()

nsdq = pd.read_csv('../data/NASDAQcompanylist.csv')

nsdq.set_index('Symbol', inplace=True)
tic_options = [{'label': nsdq.loc[tic]['Name'], 'value': tic} for tic in nsdq.index]

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        html.H3('Enter a stock symbol:',
                style = {'paddingRight': '30px'}),
        dcc.Dropdown(
            id='my_stock_ticker',
            options = tic_options,
            value='TSLA',
            multi=True)
        ],
        style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '30%'}),
    html.Div([
        html.H3('Select a start and end date:'),
        dcc.DatePickerRange(
            id='date_picker_range',
            min_date_allowed=datetime(2015,1,1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018,1,1),
            end_date=datetime(2018,12,31))
        ],
        style= {'display': 'inline-block'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'})
        ],
        style = {'display': 'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ],
            'layout': {'title': "Default Title"} 
        }
    )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_stock_ticker', 'value'),
     State('date_picker_range', 'start_date'),
     State('date_picker_range', 'end_date')]
    )
def update_graph(n_clicks, ticker_name, start_date, end_date):
    
    traces = []
    for tic in ticker_name:
        print(tic)
        df_graph = web.DataReader(
            tic,
            'stooq',
            start_date,
            end_date)
        traces.append({
            'x': df_graph.index,
            'y': df_graph['Close'],
            'name': tic})
    figure={
            'data': traces,
            'layout': {'title': ', '.join(ticker_name)+' Closing Prices'} 
        }
    return figure

if __name__ == '__main__':
    app.run_server()
