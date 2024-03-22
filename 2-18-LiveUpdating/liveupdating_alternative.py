import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import requests
import bs4
import plotly.graph_objs as go
import dash_auth

USERNAME_PASSWORD_PAIRS = [
    ['username', 'password'],
    ['JamesBond', '007']]

app = dash.Dash()

auth = dash_auth.BasicAuth(
    app,
    USERNAME_PASSWORD_PAIRS)

app.layout = html.Div([
    html.Div([
        html.H1(id='counter_text',
                children='Current BTC Price is :'),
        dcc.Graph(id='live_update_graph', style={'width': 1200}),
        dcc.Interval(id='interval_component',
                     interval=6000,
                     n_intervals=0)
    ])
 
])
 
price_history_list = []
 
 
@app.callback(Output('counter_text', 'children'),
              [Input('interval_component', 'n_intervals')])
def update_layout(n):
    price = 0
    url = 'https://au.finance.yahoo.com/quote/BTC-USD'
    r = requests.get(url, headers={'User-Agent': 'Chrome/5.0'})
    soup = bs4.BeautifulSoup(r.text, 'xml')
    price = soup.find('div', {
        'class': 'My(6px) Pos(r) smartphone_Mt(6px) W(100%) D(ib) smartphone_Mb(10px) W(100%)--mobp'}).find_all(
        'fin-streamer')[0].text
    price = price.replace(',', '')
    price_history_list.append(float(price))
    # print(price)
    # print(price_history_list)
    return f'Current BTC Price is : {float(price)}'
 
 
@app.callback(Output('live_update_graph', 'figure'),
              [Input('interval_component', 'n_intervals')])
def update_graph(n):
    fig = go.Figure(data=[go.Scatter(
        x=list(range(len(price_history_list))),
        y=price_history_list,
        mode='lines+markers'
    )])
    return fig
 
 
if __name__ == '__main__':
    app.run_server()