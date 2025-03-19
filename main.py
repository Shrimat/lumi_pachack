from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import math
import numpy as np

from load_pass_data import load_pass
from load_data import load

app = Dash(__name__)

orbit_data_1 = load("envisat")
orbit_data_2 = load("globalstar")

satellite1_station_1 = load_pass("envisat", "graz")
satellite1_station_2 = load_pass("globalstar", "graz")

satellite2_station_1 = load_pass("envisat", "herstmonceux")
satellite2_station_2 = load_pass("globalstar", "herstmonceux")

EARTH_RADIUS = 6_371_000

AXIS_SCALE = 1.5

STATION_1_LAT = 47.0678
STATION_1_LONG = 15.4942

STATION_2_LAT = 50.8674
STATION_2_LONG = 0.3361


def spheres(size, N_lat, N_lon):
    # Set up 100 points. First, do angles
    theta = np.linspace(0, 2 * np.pi, N_lat)
    phi = np.linspace(0, np.pi, N_lon)

    # Set up coordinates for points on the sphere
    x0 = size * np.outer(np.cos(theta), np.sin(phi))
    y0 = size * np.outer(np.sin(theta), np.sin(phi))
    z0 = size * np.outer(np.ones(N_lat), np.cos(phi))

    # Set up trace
    trace = go.Surface(x=x0, y=y0, z=z0, colorscale=[[0, 'rgb(0,0,255)'], [1, 'rgb(0,0,255)']])
    trace.update(showscale=False)

    return trace


@app.callback(
    Output('example-graph-1', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def make_figure(k):
    trace_without_image = spheres(EARTH_RADIUS, 20, 20)
    graphdata = go.Figure(
        data=[
            go.Scatter3d(
                x=orbit_data_1[max(k-50, 0):k+1, 0],
                y=orbit_data_1[max(k-50, 0):k+1, 1],
                z=orbit_data_1[max(k-50, 0):k+1, 2],
                mode="lines",
                name="Envisat",
                line=dict(color="red", colorscale='Viridis')),
            go.Scatter3d(
                x=orbit_data_2[max(k-50, 0):k+1, 0],
                y=orbit_data_2[max(k-50, 0):k+1, 1],
                z=orbit_data_2[max(k-50, 0):k+1, 2],
                mode="lines",
                name="Globalstar",
                line=dict(color="green", colorscale='Viridis')),
            # go.Scatter3d(
            #     x=[0.],
            #     y=[0.],
            #     z=[0.],
            #     mode="markers",
            #     name="Earth",
            #     marker=dict(color="blue", size=20)),
            trace_without_image,
            go.Scatter3d(
                x=[EARTH_RADIUS*math.cos(STATION_1_LAT)*math.cos(STATION_1_LONG)],
                y=[EARTH_RADIUS*math.cos(STATION_1_LAT)*math.sin(STATION_1_LONG)],
                z=[EARTH_RADIUS*math.sin(STATION_1_LAT)],
                mode="markers",
                name="Station 1",
                marker=dict(color="yellow", size=2)),
            go.Scatter3d(
                x=[EARTH_RADIUS * math.cos(STATION_2_LAT) * math.cos(STATION_2_LONG)],
                y=[EARTH_RADIUS * math.cos(STATION_2_LAT) * math.sin(STATION_2_LONG)],
                z=[EARTH_RADIUS * math.sin(STATION_2_LAT)],
                mode="markers",
                name="Station 2",
                marker=dict(color="orange", size=2)),
            go.Scatter3d(
                x=[orbit_data_1[k, 0]],
                y=[orbit_data_1[k, 1]],
                z=[orbit_data_1[k, 2]],
                mode="markers",
                name="Envisat",
                marker=dict(color="red", size=2),
                showlegend=False),
            go.Scatter3d(
                x=[orbit_data_2[k, 0]],
                y=[orbit_data_2[k, 1]],
                z=[orbit_data_2[k, 2]],
                mode="markers",
                name="Globalstar",
                marker=dict(color="green", size=2),
                showlegend=False),
        ])
    graphdata['layout']['uirevision'] = True
    graphdata.update_layout(
        paper_bgcolor="black",
        uirevision=True,
        scene=dict(
            xaxis=dict(nticks=4, range=[-AXIS_SCALE *
                   EARTH_RADIUS, AXIS_SCALE * EARTH_RADIUS], autorange=False, visible = False),
            yaxis=dict(nticks=4, range=[-AXIS_SCALE *
                   EARTH_RADIUS, AXIS_SCALE * EARTH_RADIUS], autorange=False, visible = False),
            zaxis=dict(nticks=4, range=[-AXIS_SCALE *
                   EARTH_RADIUS, AXIS_SCALE * EARTH_RADIUS], autorange=False, visible = False),
            aspectratio = dict(x=1, y=1, z=1))
    )
    return graphdata


def get_graph_data(data1, data2, k):
    graphdata = go.Figure(data=[
        go.Scatterpolar(
            r=data1[max(k - 50, 0):k + 1, 1],
            theta=data1[max(k - 50, 0):k + 1, 0],
            mode='lines',
            name="Envisat",
            line=dict(color="red")
        ),
        go.Scatterpolar(
            r=data2[max(k - 50, 0):k + 1, 1],
            theta=data2[max(k - 50, 0):k + 1, 0],
            mode='lines',
            name="Globalstar",
            line=dict(color="green")
        ),
        go.Scatterpolar(
            r=[data1[k, 1]],
            theta=[data1[k, 0]],
            mode='markers',
            name="Envisat",
            showlegend=False,
            marker=dict(color="red")
        ),
        go.Scatterpolar(
            r=[data2[k, 1]],
            theta=[data2[k, 0]],
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


@app.callback(
    Output('example-graph-2', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def make_figure_2(k):
    return get_graph_data(satellite1_station_1, satellite1_station_2, k)


@app.callback(
    Output('example-graph-3', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def make_figure_3(k):
    return get_graph_data(satellite2_station_1, satellite2_station_2, k)


app.layout = html.Div([
    dbc.Row(dbc.Col(html.H1(children='Lumi Satellite Orbital Data'))),
    dbc.Row(dbc.Col(dcc.Graph(id='example-graph-1', figure=go.Figure()))),
    dbc.Row([
        dbc.Col(dcc.Graph(id='example-graph-2', figure=go.Figure()), width=6),
        dbc.Col(dcc.Graph(id='example-graph-3', figure=go.Figure()), width=6)
    ]),
    dcc.Interval(
        id='graph-update',
        interval=500,
        n_intervals=0
    )
])

if __name__ == '__main__':
    app.run(debug=True)
