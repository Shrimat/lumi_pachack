from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from load_data import load

# df = px.data.iris()

# df_numpy = np.array([[0., 0., 0.], [1., 1., 1.]])
# df = pd.DataFrame(df_numpy, columns = ['x','y',"z"])

def plot_data(data):
	fig = go.Figure(data=[go.Scatter3d(
		x=data[:, 0],
		y=data[:, 1],
		z=data[:, 2],
		mode='markers',
		marker=dict(
			size=3,
			colorscale='Viridis',
			opacity=1
		)
	)])
	# fig = px.scatter_3d(df, x='x', y='y', z='z', opacity = 0.5, size_max = 5)

	app = Dash(__name__)

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

	app.run_server(debug=True)

if __name__ == '__main__':
	plot_data(load("envisat"))
	