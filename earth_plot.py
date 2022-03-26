import numpy as np
import plotly.graph_objects as go


def earth_plot(dist, size):
    # Set up 100 points. First, do angles
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    # Set up coordinates for points on the sphere
    x0 = dist + size * np.outer(np.cos(theta), np.sin(phi))
    y0 = size * np.outer(np.sin(theta), np.sin(phi))
    z0 = size * np.outer(np.ones(100), np.cos(phi))

    # Set up trace
    trace = go.Surface(x=x0, y=y0, z=z0)
    trace.update(showscale=False)

    return trace