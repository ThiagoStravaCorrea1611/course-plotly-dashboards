#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# create a DataFrame from the .csv file:
df_data_graph = pd.read_csv("..\\Data\\mocksurvey.csv", index_col=0)

# create traces using a list comprehension:
data_1 = [go.Bar(
            x=df_data_graph.index,
            y=df_data_graph[ans],
            name=ans) for ans in df_data_graph.columns]

data_2 = [go.Bar(
            x=df_data_graph[ans],
            y=df_data_graph.index,
            name=ans,
            orientation='h') for ans in df_data_graph.columns]

layout = go.Layout(
    title='Mock Survey Results',
    barmode='stack')

fig_1 = go.Figure(
    data=data_1,
    layout=layout
)

fig_2 = go.Figure(
    data=data_2,
    layout=layout
)

pyo.plot(
    fig_1,
    filename = 'my_solution_1.html')

pyo.plot(
    fig_2,
    filename = 'my_solution_2.html')



# create a layout, remember to set the barmode here





# create a fig from data & layout, and plot the fig.
