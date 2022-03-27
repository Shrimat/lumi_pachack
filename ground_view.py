from dash import Dash, html, dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output

import main


def plot_data_2(data1, data2):
    fig = go.Figure(data=[
        go.Scatterpolar(
            r=data1[:, 1],
            theta=data1[:, 0],
            mode='lines',
            name="Envisat",
            line=dict(color="red")
        ),
        go.Scatterpolar(
            r=data2[:, 1],
            theta=data2[:, 0],
            mode='lines',
            name="Globalstar",
            line=dict(color="green")
        ),
        go.Scatterpolar(
            r=data1[0, 1],
            theta=data1[0, 0],
            mode='markers',
            name="Envisat",
            showlegend=False,
            marker=dict(color="red")
        ),
        go.Scatterpolar(
            r=data2[0, 1],
            theta=data2[0, 0],
            mode='markers',
            name="Globalstar",
            showlegend=False,
            marker=dict(color="green")
        )])

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="black",
        polar=dict(
            radialaxis=dict(range=[0, 90]),
        )
    )


@main.app.callback(
    Output('example-graph-2', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def make_figure(k):
    graphdata = go.Figure(data=[
        go.Scatterpolar(
            r=main.satellite1_station_1[max(k - 50, 0):k + 1, 1],
            theta=main.satellite1_station_1[max(k - 50, 0):k + 1, 0],
            mode='lines',
            name="Envisat",
            line=dict(color="red")
        ),
        go.Scatterpolar(
            r=main.satellite1_station_2[max(k - 50, 0):k + 1, 1],
            theta=main.satellite1_station_2[max(k - 50, 0):k + 1, 0],
            mode='lines',
            name="Globalstar",
            line=dict(color="green")
        ),
        go.Scatterpolar(
            r=[main.satellite1_station_1[k, 1]],
            theta=[main.satellite1_station_1[k, 0]],
            mode='markers',
            name="Envisat",
            showlegend=False,
            marker=dict(color="red")
        ),
        go.Scatterpolar(
            r=[main.satellite1_station_2[k, 1]],
            theta=[main.satellite1_station_2[k, 0]],
            mode='markers',
            name="Globalstar",
            showlegend=False,
            marker=dict(color="green")
        )])
    graphdata.update_layout(
        template="plotly_dark",
        uirevision=True,
        paper_bgcolor="black",
        polar=dict(
            radialaxis=dict(range=[0, 90]),
        )
    )
    return graphdata
