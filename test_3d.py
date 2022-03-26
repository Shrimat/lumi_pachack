import plotly.graph_objects as go
import numpy as np

EARTH_RADIUS = 6_371_000


def plot_data(data1, data2):
	trace = spheres(EARTH_RADIUS, "Earth")
	fig = go.Figure(data=[go.Scatter3d(
		x=data1[:, 0],
		y=data1[:, 1],
		z=data1[:, 2],
		mode='lines',
		name = "Envisat",
		line = dict(
			#size=size,
			color = "orange",
			colorscale='Viridis',
		)
	),go.Scatter3d(
		x=data2[:, 0],
		y=data2[:, 1],
		z=data2[:, 2],
		mode='lines',
		name = "Globalstar",
		line = dict(
			#size=size,
			color = "green",
			colorscale='Viridis'))
	,trace])

	return fig


def spheres(size, clr, dist=0):
	# Set up 100 points. First, do angles
	theta = np.linspace(0, 2 * np.pi, 100)
	phi = np.linspace(0, np.pi, 100)

	# Set up coordinates for points on the sphere
	x0 = dist + size * np.outer(np.cos(theta), np.sin(phi))
	y0 = size * np.outer(np.sin(theta), np.sin(phi))
	z0 = size * np.outer(np.ones(100), np.cos(phi))

	# Set up trace
	trace = go.Surface(x=x0, y=y0, z=z0, colorscale=clr)
	trace.update(showscale=False)

	return trace
