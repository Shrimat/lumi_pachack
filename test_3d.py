import plotly.graph_objects as go


def plot_data(data1, data2, data3):
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
	,go.Scatter3d(
		x=data3[:, 0],
		y=data3[:, 1],
		z=data3[:, 2],
		mode='markers',
		name = "Earth",
		marker = dict(
			size=20,
			color = "blue",
			colorscale='Viridis'))])

	return fig
