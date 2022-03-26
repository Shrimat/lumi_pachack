from dash import Dash, html, dcc
import plotly.graph_objects as go
from load_data import load
from earth_plot import earth_plot
from app import app

def plot_data(df):
    #fig = px.scatter_3d(df, x='x', y='y', z='z')
    fig = go.Figure(data=[earth_plot(20, 5)])

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
    plot_data(load("envisat"))
