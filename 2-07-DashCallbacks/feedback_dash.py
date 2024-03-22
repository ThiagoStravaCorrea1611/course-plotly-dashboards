import dash
from dash import dcc
from dash import html
import dash_table
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd

df_graph = pd.read_csv('../data/nextier_test_dash_data_v2.csv')
df_graph.sort_values(by='sensor_ts', inplace=True)

# Available dates dropdown menu 
dates_options = []
for dates in df_graph['ref_date_cst'].unique():
    dates_options.append({'label':str(dates),'value':dates})

# Displayed Table
events = df_graph[df_graph.event == 1][[
    'ref_date_cst', 'unit_parent_number', 'stage_id','sensor_ts', "make", "model"]]
# Add first column with empty boxes:
events.insert(0, 'Select', '⬜')

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id='date-picker',
        options=dates_options,
        value=df_graph['ref_date_cst'].min()),
    html.Hr(),
    dcc.Dropdown(id='unit-picker'),
    html.Hr(),
    dcc.Dropdown(id='stage-picker'),
    html.Hr(),
    dash_table.DataTable(
        id='feedback-table',
        columns=[{"name": i, "id": i} for i in events.columns],
        editable=False,
        style_as_list_view= True,
        style_data_conditional=[
            {'if': {'state': 'active'},'backgroundColor': 'white', 'border': '1px solid white'},
            {'if': {'column_id': 'Company Name'}, 'textAlign': 'left', 'text-indent': '10px', 'width':100},
            ],
        fixed_rows={'headers': True},
        style_data={"font-size" : "14px", 'width': 15, "background":"white", 'text-align': 'center'}),
    #dcc.Graph(id='graph')
    
])

# Update available units
@app.callback(
    Output('unit-picker', 'options'),
    Input('date-picker', 'value'))
def set_units_options(selected_date):
    available_units = df_graph[df_graph['ref_date_cst'] == selected_date]\
        .unit_parent_number\
            .unique()\
                .tolist ()
    return [{'label': i, 'value': i} for i in available_units]

@app.callback(
    Output('unit-picker', 'value'),
    Input('unit-picker', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


# Update available stages
@app.callback(
    Output('stage-picker', 'options'),
    [
        Input('date-picker', 'value'),
        Input('unit-picker', 'value')
    ])
def set_units_options(selected_date, selected_unit):
    condition = ((df_graph['ref_date_cst'] == selected_date)
                 & (df_graph['unit_parent_number'] == selected_unit))
    available_stages = df_graph[condition]\
        .stage_id\
            .unique()\
                .tolist ()
    return [{'label': i, 'value': i} for i in available_stages]

@app.callback(
    Output('stage-picker', 'value'),
    Input('stage-picker', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


# Update table
@app.callback(
    Output('feedback-table', 'data'),
    [
        Input('date-picker', 'value'),
        Input('unit-picker', 'value'),
        Input('stage-picker', 'value'),
    ])
def update_table_data(selected_date, selected_unit, selected_stage):
    condition = ((events['ref_date_cst'] == selected_date)
                 & (events['unit_parent_number'] == selected_unit)
                 & (events['stage_id'] == selected_stage))
    updated_table = events[condition]
    
    return updated_table.to_dict('records')

# Update graph
@app.callback(
    Output('graph', 'figure'),
    [
        Input('date-picker', 'value'),
        Input('unit-picker', 'value'),
        Input('stage-picker', 'value'),
    ])
def update_graph(selected_date, selected_unit, selected_stage):
    condition = ((df_graph['ref_date_cst'] == selected_date)
                 & (df_graph['unit_parent_number'] == selected_unit)
                 & (df_graph['stage_id'] == selected_stage))
    updated_df_graph = df_graph[condition]
    

#fig = go.Figure()
#
#fig.add_trace(go.Scatter(
#    x=df_graph.sensor_ts,
#    y=df_graph.eng_oil_press,
#    name="eng_oil_press"
#))
#
#
#fig.add_trace(go.Scatter(
#    x=df_graph.sensor_ts,
#    y=df_graph.eng_fuel_press,
#    name="eng_fuel_press",
#    yaxis="y2"
#))
#fig.add_trace(go.Scatter(
#    x=df_graph.sensor_ts,
#    y=df_graph.rpm,
#    name="rpm",
#    yaxis="y3"
#))
#fig.add_trace(go.Scatter(
#    x=df_graph.sensor_ts,
#    y=df_graph.eng_dgb_mode,
#    name="eng_dgb_mode",
#    yaxis="y4"
#))
#
#
## Create axis objects
#fig.update_layout(
#    xaxis=dict(
#        domain=[0.1, 0.9]
#    ),
#    yaxis=dict(
#        title="eng_oil_press",
#        titlefont=dict(
#            color="#1f77b4"
#        ),
#        tickfont=dict(
#            color="#1f77b4"
#        ),
#        showgrid=False
#    ),
#    yaxis2=dict(
#        title="eng_fuel_press",
#        titlefont=dict(
#            color="#ff7f0e"
#        ),
#        tickfont=dict(
#            color="#ff7f0e"
#        ),
#        anchor="free",
#        overlaying="y",
#        side="left",
#        position=0.05,
#        showgrid=False
#    ),
#    yaxis3=dict(
#        title="rpm",
#        titlefont=dict(
#            color="#d62728"
#        ),
#        tickfont=dict(
#            color="#d62728"
#        ),
#        anchor="x",
#        overlaying="y",
#        side="right",
#        showgrid=False
#    ),
#    yaxis4=dict(
#        title="eng_dgb_mode",
#        titlefont=dict(
#            color="#9467bd"
#        ),
#        tickfont=dict(
#            color="#9467bd"
#        ),
#        anchor="free",
#        overlaying="y",
#        side="right",
#        position=0.95,
#        showgrid=False
#    )
#)
#
#
## Add vertical lines for markers
#events_ts = list(df_graph[df_graph.event == 1].sensor_ts)
#for sensor_ts in events_ts:
#  fig.add_trace(go.Scatter(
#      x=[sensor_ts, sensor_ts],
#      y=[0, 85],
#      mode='lines',
#      line=dict(color='orange', width=1, dash='dash'),
#      name='event'
#      ))
#
#
## Update layout properties
#fig.update_layout(
#    title_text=f"Stage: {stage}",
#    width=1000,
#    showlegend=False,
#)
#    
#    
#return updated_table.to_dict('records')


# Enable selection
#@app.callback(Output("feedback-table", "data"),
#              [Input('feedback-table', 'active_cell')])
#def update_true_positives(cell,  data):
#    if cell["column_id"] == 'Select':
#        # takes info for some columns in the row selected
#        true_positive_ts = data[cell["row"]]["sensor_ts"]
#
#        # 4) Change the figure of the box selected
#        if data[cell["row"]]["Select"] == '⬜':
#            data[cell["row"]]["Select"] = '✅'
#        else:
#        # 5) if the user unselect the selected box:
#            data[cell["row"]]["Select"] = '⬜'
#
#        # if other column is selected do nothing:
#    else:
#        raise PreventUpdate
#
#    return data
        

if __name__ == '__main__':
    app.run_server()