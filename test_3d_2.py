from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from load_data import load
from dash.dependencies import Input, Output

def plot_data(data1, data2, data3):
    Re = 6371000
    axisScale = 1.5
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=data1[:, 0],
                y=data1[:, 1],
                z=data1[:, 2],
                mode='lines',
                name="Envisat",
                line=dict(
                    color="red",
                    colorscale='Viridis')),
            go.Scatter3d(
                x=data2[:, 0],
                y=data2[:, 1],
                z=data2[:, 2],
                mode='lines',
                name="Globalstar",
                line=dict(
                    color="green",
                    colorscale='Viridis')),
            go.Scatter3d(
                x=data3[:, 0],
                y=data3[:, 1],
                z=data3[:, 2],
                mode='markers',
                name="Earth",
                marker=dict(
                    size=20,
                    color="blue",
                    colorscale='Viridis')),
            go.Scatter3d(
                x=[data1[0, 0]],
                y=[data1[0, 1]],
                z=[data1[0, 2]],
                mode="markers",
                name="Envisat",
                marker=dict(color="red", size=2),
                showlegend=False),
            go.Scatter3d(
                x=[data2[0, 0]],
                y=[data2[0, 1]],
                z=[data2[0, 2]],
                mode="markers",
                name="Globalstar",
                marker=dict(color="green", size=2),
                showlegend=False)],

        layout=go.Layout(
            title="Satellite Information",
            hovermode="closest",
            uirevision=True)
            # updatemenus=[dict(
            #     type="buttons",
            #     buttons=[dict(label="Play",
            #                   method="animate",
            #                   args=[None, {"frame": {"duration": 5},
            #                       "transition": {"duration": 5}}])
            #              ])]),
    )

    fig.update_layout(
        paper_bgcolor="black",
        uirevision=True,
        scene=dict(
            xaxis=dict(nticks=4, range=[-axisScale *
                       Re, axisScale * Re], autorange=False, visible = False),
            yaxis=dict(nticks=4, range=[-axisScale *
                       Re, axisScale * Re], autorange=False, visible = False),
            zaxis=dict(nticks=4, range=[-axisScale * 
            	       Re, axisScale * Re], autorange=False, visible = False),
            aspectratio = dict(x=1, y=1, z=1),
            uirevision=True)
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
        graphdata = go.Figure(
            data=[
                go.Scatter3d(
                    x=data1[max(k-50, 0):k+1, 0],
                    y=data1[max(k-50, 0):k+1, 1],
                    z=data1[max(k-50, 0):k+1, 2],
                    mode="lines",
                    name="Envisat",
                    line=dict(color="red", colorscale='Viridis')),
                go.Scatter3d(
                    x=data2[max(k-50, 0):k+1, 0],
                    y=data2[max(k-50, 0):k+1, 1],
                    z=data2[max(k-50, 0):k+1, 2],
                    mode="lines",
                    name="Globalstar",
                    line=dict(color="green", colorscale='Viridis')),
                go.Scatter3d(
                    x=[data3[0, 0]],
                    y=[data3[0, 1]],
                    z=[data3[0, 2]],
                    mode="markers",
                    name="Earth",
                    marker=dict(color="blue", size=20)),
                go.Scatter3d(
                    x=[data1[k, 0]],
                    y=[data1[k, 1]],
                    z=[data1[k, 2]],
                    mode="markers",
                    name="Envisat",
                    marker=dict(color="red", size=2),
                    showlegend=False),
                go.Scatter3d(
                    x=[data2[k, 0]],
                    y=[data2[k, 1]],
                    z=[data2[k, 2]],
                    mode="markers",
                    name="Globalstar",
                    marker=dict(color="green", size=2),
                    showlegend=False),
            ])
            # layout=go.Layout(
            #     title="Satellite Information",
            #     hovermode="closest",
            #     uirevision=True)
        graphdata['layout']['uirevision'] = True
        graphdata.update_layout(
            paper_bgcolor="black",
            uirevision=True,
            scene=dict(
                xaxis=dict(nticks=4, range=[-axisScale *
                       Re, axisScale * Re], autorange=False, visible = False),
                yaxis=dict(nticks=4, range=[-axisScale *
                       Re, axisScale * Re], autorange=False, visible = False),
                zaxis=dict(nticks=4, range=[-axisScale * 
                       Re, axisScale * Re], autorange=False, visible = False),
                aspectratio = dict(x=1, y=1, z=1))
        )
        return graphdata

    app.run_server(debug=True)


if __name__ == '__main__':

    plot_data(load("envisat"), load("globalstar"), np.array([[0., 0., 0.]]))




