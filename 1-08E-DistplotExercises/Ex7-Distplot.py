#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df_graph = pd.read_csv('../data/iris.csv')

# Define a data variable
hist_data = [
    df_graph[df_graph['class']==iris_class]['petal_length']
    for iris_class in df_graph['class'].unique()]
group_labels = df_graph['class'].unique()

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.5, 0.5, 0.5])
pyo.plot(fig, filename='my_solution_distplot.html')