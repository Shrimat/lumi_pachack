import plotly.graph_objects as go
import numpy as np
from PIL import Image

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


def plot_data(data1, data2):
    texture = np.asarray(Image.open('earth.jpg')).T
    trace = spheres(EARTH_RADIUS, texture)
    fig = go.Figure(data=[go.Scatter3d(
        x=data1[:, 0],
        y=data1[:, 1],
        z=data1[:, 2],
        mode='lines',
        name="Envisat",
        line=dict(
            # size=size,
            color="orange",
            colorscale='Viridis',
        )
    ), go.Scatter3d(
        x=data2[:, 0],
        y=data2[:, 1],
        z=data2[:, 2],
        mode='lines',
        name="Globalstar",
        line=dict(
            # size=size,
            color="green",
            colorscale='Viridis'))
        , trace])

    return fig


def spheres(size, texture):
    N_lat = int(texture.shape[0])
    N_lon = int(texture.shape[1])
    # Set up 100 points. First, do angles
    theta = np.linspace(0, 2 * np.pi, N_lat)
    phi = np.linspace(0, np.pi, N_lon)

    # Set up coordinates for points on the sphere
    x0 = size * np.outer(np.cos(theta), np.sin(phi))
    y0 = size * np.outer(np.sin(theta), np.sin(phi))
    z0 = size * np.outer(np.ones(N_lat), np.cos(phi))

    # Set up trace
    trace = go.Surface(x=x0, y=y0, z=z0, surfacecolor=texture, colorscale=COLOR_SCALE)
    trace.update(showscale=False)

    return trace
