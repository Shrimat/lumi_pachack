from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

df = px.data.iris()

df_numpy = np.array([[0., 0., 0.], [1., 1., 1.]])
df = pd.DataFrame(df_numpy, columns = ['x','y',"z"])
fig = px.scatter_3d(df, x='x', y='y', z='z')

app = Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)