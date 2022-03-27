from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from load_pass_data import load_pass
from dash.dependencies import Input, Output

def plot_data(data1, data2):
    fig = go.Figure(data=[
        go.Scatterpolar(
            r = data1[:, 1],
            theta = data1[:, 0],
            mode = 'lines',
            name = "Envisat",
            line=dict(color="red")
        ),
        go.Scatterpolar(
            r = data2[:, 1],
            theta = data2[:, 0],
            mode = 'lines',
            name = "Globalstar",
            line=dict(color="green")
        ),
        go.Scatterpolar(
            r = data1[0, 1],
            theta = data1[0, 0],
            mode = 'markers',
            name = "Envisat",
            showlegend=False,
            marker=dict(color="red")
        ),
        go.Scatterpolar(
            r = data2[0, 1],
            theta = data2[0, 0],
            mode = 'markers',
            name = "Globalstar",
            showlegend=False,
            marker=dict(color="green")
        )])

    fig.update_layout(
        polar = dict(
            radialaxis = dict(range=[0, 90]),
        )
    )

    app = Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(id = "test", children='Hello Dash'),
        html.Div(children='''
			Dash: A web application framework for your data.
		'''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
        dcc.Interval(
            id='graph-update',
            interval= 50,
            n_intervals=0
        ),
    ])

    @app.callback(Output('example-graph', 'figure'), [Input('graph-update', 'n_intervals')])
    def make_figure(k):
        graphdata = go.Figure(data=[
            go.Scatterpolar(
                r = data1[max(k-50, 0):k+1, 1],
                theta = data1[max(k-50, 0):k+1, 0],
                mode = 'lines',
                name = "Envisat",
                line=dict(color="red")
            ),
            go.Scatterpolar(
                r = data2[max(k-50, 0):k+1, 1],
                theta = data2[max(k-50, 0):k+1, 0],
                mode = 'lines',
                name = "Globalstar",
                line=dict(color="green")
            ),
            go.Scatterpolar(
                r = [data1[k, 1]],
                theta = [data1[k, 0]],
                mode = 'markers',
                name = "Envisat",
                showlegend=False,
                marker=dict(color="red")
            ),
            go.Scatterpolar(
                r = [data2[k, 1]],
                theta = [data2[k, 0]],
                mode = 'markers',
                name = "Globalstar",
                showlegend=False,
                marker=dict(color="green")
            )])
        graphdata.update_layout(
        	uirevision=True,
            polar = dict(
                radialaxis = dict(range=[0, 90]),
            )
        )
        return graphdata

    app.run_server(debug=True)


if __name__ == '__main__':
    plot_data(load_pass("envisat", "graz"), load_pass("globalstar", "graz"))




