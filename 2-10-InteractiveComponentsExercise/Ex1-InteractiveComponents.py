#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    dcc.RangeSlider(-10, 10, 1,
                    count=1,
                    value=[-5, 5],
                    id='range-slider'),
    html.Hr(),
    html.Div(id='multiplication')
])

@app.callback(
    Output('multiplication', 'children'),
    [Input('range-slider', 'value')])
def callback_a(range_selection):
    product = range_selection[0]*range_selection[1]
    ans = f"The product output is: {range_selection[0]}x{range_selection[1]} = {product}"
    return ans


if __name__ == '__main__':
    app.run_server()










# Create a Dash callback:






# Add the server clause:
