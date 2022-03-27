from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import numpy as np

from load_pass_data import load_pass
from load_data import load
from PIL import Image

app = Dash(__name__)

orbit_data_1 = load("envisat")
orbit_data_2 = load("globalstar")

satellite1_station_1 = load_pass("envisat", "graz")
satellite1_station_2 = load_pass("globalstar", "graz")

satellite2_station_1 = load_pass("envisat", "herstmonceux")
satellite2_station_2 = load_pass("globalstar", "herstmonceux")

EARTH_RADIUS = 6_371_000

COLOR_SCALE = [[0.0, 'rgb(30, 59, 117)'],
              [0.1, 'rgb(46, 68, 21)'],
              [0.2, 'rgb(74, 96, 28)'],
              [0.3, 'rgb(115,141,90)'],
              [0.4, 'rgb(122, 126, 75)'],
              [0.6, 'rgb(122, 126, 75)'],
              [0.7, 'rgb(141,115,96)'],
              [0.8, 'rgb(223, 197, 170)'],
              [0.9, 'rgb(237,214,183)'],
              [1.0, 'rgb(255, 255, 255)']]

AXIS_SCALE = 1.5


def plot_data_1(data1, data2):
    # texture = np.asarray(Image.open('earth-min.jpg')).T
    # N_lat = int(texture.shape[0])
    # N_lon = int(texture.shape[1])
    # trace_without_image = spheres(EARTH_RADIUS, None, "Earth", 100, 100)
    # trace_with_image = spheres(EARTH_RADIUS, texture, COLOR_SCALE, N_lat, N_lon)

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
                x=[0.],
                y=[0.],
                z=[0.],
                mode="markers",
                name="Earth",
                marker=dict(color="blue", size=20)),
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
            uirevision=True,
            # updatemenus=[dict(
            #     type="buttons",
            #     buttons=[
            #         {
            #             "args": [None, {"frame": {"duration": 5},
            #                             "fromcurrent": True, "transition": {"duration": 5,
            #                                                                 "easing": "quadratic-in-out"}}],
            #             "label": "Play",
            #             "method": "animate"
            #         },
            #         {
            #             "args": [[None], {"frame": {"duration": 0},
            #                               "mode": "immediate",
            #                               "transition": {"duration": 0}}],
            #             "label": "Pause",
            #             "method": "animate"
            #         }
            #     ])]
        ))

    fig.update_layout(
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
    return fig


def spheres(size, texture, clr, N_lat, N_lon):
    # Set up 100 points. First, do angles
    theta = np.linspace(0, 2 * np.pi, N_lat)
    phi = np.linspace(0, np.pi, N_lon)

    # Set up coordinates for points on the sphere
    x0 = size * np.outer(np.cos(theta), np.sin(phi))
    y0 = size * np.outer(np.sin(theta), np.sin(phi))
    z0 = size * np.outer(np.ones(N_lat), np.cos(phi))

    # Set up trace
    trace = go.Surface(x=x0, y=y0, z=z0, surfacecolor=texture, colorscale=clr)
    trace.update(showscale=False)

    return trace


@app.callback(
    Output('example-graph-1', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def make_figure(k):
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
            go.Scatter3d(
                x=[0.],
                y=[0.],
                z=[0.],
                mode="markers",
                name="Earth",
                marker=dict(color="blue", size=20)),
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


@app.callback(
    Output('example-graph-2', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def make_figure_2(k):
    graphdata = go.Figure(data=[
        go.Scatterpolar(
            r=satellite1_station_1[max(k - 50, 0):k + 1, 1],
            theta=satellite1_station_1[max(k - 50, 0):k + 1, 0],
            mode='lines',
            name="Envisat",
            line=dict(color="red")
        ),
        go.Scatterpolar(
            r=satellite1_station_2[max(k - 50, 0):k + 1, 1],
            theta=satellite1_station_2[max(k - 50, 0):k + 1, 0],
            mode='lines',
            name="Globalstar",
            line=dict(color="green")
        ),
        go.Scatterpolar(
            r=[satellite1_station_1[k, 1]],
            theta=[satellite1_station_1[k, 0]],
            mode='markers',
            name="Envisat",
            showlegend=False,
            marker=dict(color="red")
        ),
        go.Scatterpolar(
            r=[satellite1_station_2[k, 1]],
            theta=[satellite1_station_2[k, 0]],
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

# fig_1 = plot_data_1(orbit_data_1, orbit_data_2)
#
# satellite1_fig = plot_data_2(satellite1_station_1, satellite1_station_2)
# #satellite2_fig = plot_data_2(satellite2_station_1, satellite2_station_2)

app.layout = html.Div(children=[
    dbc.Row(dbc.Col(html.H1(children='Lumi Satellite Orbital Data'), width=6)),
    html.Div(children='''
        Orbits for Envisat and Globalstar satellites
    '''),
    dcc.Graph(
        id='example-graph-1',
        figure=go.Figure()
    ),
    dcc.Graph(
        id='example-graph-2',
        figure=go.Figure()
    ),
    dcc.Graph(
        id='example-graph-3',
        figure=go.Figure()
    ),
    dcc.Interval(
        id='graph-update',
        interval=200,
        n_intervals=0
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
