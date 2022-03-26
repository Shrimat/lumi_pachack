from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from load_data import load

# df = px.data.iris()

# df_numpy = np.array([[0., 0., 0.], [1., 1., 1.]])
# df = pd.DataFrame(df_numpy, columns = ['x','y',"z"])

def plot_data(data1, data2, data3):
	fig = go.Figure(data=[go.Scatter3d(
		x=data1[:, 0],
		y=data1[:, 1],
		z=data1[:, 2],
		mode='lines',
		line = dict(
			#size=size,
			colorscale='Viridis',
		)
	),go.Scatter3d(
		x=data2[:, 0],
		y=data2[:, 1],
		z=data2[:, 2],
		mode='lines',
		line = dict(
			#size=size,
			colorscale='Viridis'))
	,go.Scatter3d(
		x=data3[:, 0],
		y=data3[:, 1],
		z=data3[:, 2],
		mode='markers',
		marker = dict(
			size=20,
			colorscale='Viridis'))])
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

def merge_data(data1, data2):
	return np.append(data1, data2, axis = 0)

if __name__ == '__main__':
	data = merge_data(load("envisat"), load("globalstar"))
	data = merge_data(data, np.array([[0, 0, 0]]))
	plot_data(load("envisat"), load("globalstar"), np.array([[0., 0., 0.]]))
	