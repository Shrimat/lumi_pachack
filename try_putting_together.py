from dash import Dash, html, dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from load_data import load
import dash_bootstrap_components as dbc


def plot_data(data1, data2, data3):
    Re = 6371000
    axisScale = 2
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=data1[:, 0],
                y=data1[:, 1],
                z=data1[:, 2],
                mode='lines',
                name="Envisat",
                line=dict(
                    color="orange",
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
                    colorscale='Viridis'))
                    ],

        layout=go.Layout(
            title="The Earth and its satellites",
            hovermode="closest",
            updatemenus=[dict(
                type="buttons",
                buttons=[
                    {
                        "args": [None, {"frame": {"duration": 5},
                                        "fromcurrent": True, "transition": {"duration": 5,
                                                                            "easing": "quadratic-in-out"}}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0},
                                          "mode": "immediate",
                                          "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ])]),

        frames=[go.Frame(
            data=[
                go.Scatter3d(
                    x=[data1[k, 0]],
                    y=[data1[k, 1]],
                    z=[data1[k, 2]],
                    mode="markers",
                    marker=dict(color="red", size=2)),
                go.Scatter3d(
                    x=[data2[k, 0]],
                    y=[data2[k, 1]],
                    z=[data2[k, 2]],
                    mode="markers",
                    marker=dict(color="green", size=2))

            ]
        )for k in range(len(data1))])
    # fig.layout.autosize = True
    fig.update_layout(
        paper_bgcolor="black",
        scene=dict(
            xaxis=dict(nticks=4, range=[-axisScale *
                       Re, axisScale * Re], autorange=False),
            yaxis=dict(nticks=4, range=[-axisScale *
                       Re, axisScale * Re], autorange=False),
            zaxis=dict(nticks=4, range=[-axisScale *
                       Re, axisScale * Re], autorange=False),
            aspectratio=dict(x=1, y=1, z=1)),
    )


    test_var=2

    ####################################################################################
    detailed_parameters = go.Figure(data=[go.Table(
    header=dict(
        values=list(('1','2','3')),
        line_color='darkslategray',
        fill_color = 'lightskyblue',
        align='center'),
    cells=dict(
        values=[test_var,2,3],
        line_color='darkslategray',
        fill_color='lightcyan',
        align='center'))

])
    ####################################################################################
    # $$$$$$$$$$$$$$$$$$
    scatter = fig.data[0]
    fig.layout.hovermode = 'closest'

    # create our callback function
    def update_point():
        test_var+=1


    scatter.on_click(update_point)
    detailed_parameters.update_traces()

    ####################################################################################
    app = Dash(__name__)
    app.layout = html.Div(
        children=[
            html.H1(children='PacHack - Lumi Space'),
            html.Div(children='''A visualisation of satellite paths'''),
            dbc.Row(
                [
                    dcc.Graph(id='satellite_graph', figure=fig, style={
                        'width': '100vh', 'height': '70vh'}),
                    dcc.Graph(id='satellite_graph2', figure=detailed_parameters, style={
                        'width': '100vh', 'height': '70vh'}),
                ],
                align="center",
                style=dict(display='flex', margin='auto'),
            ), ])
    app.run_server(debug=True)
    ####################################################################################

if __name__ == '__main__':
    plot_data(load("envisat"), load("globalstar"), np.array([[0., 0., 0.]]))
