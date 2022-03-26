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
	axisD = 10E6
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=data1[:, 0],
                y=data1[:, 1],
                z=data1[:, 2],
                mode='lines',
                name="Envisat",
                line=dict(
                    # size=size,
                    color="orange",
                    colorscale='Viridis')),
            go.Scatter3d(
                x=data2[:, 0],
                y=data2[:, 1],
                z=data2[:, 2],
                mode='lines',
                name="Globalstar",
                line=dict(
                    # size=size,
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
                    colorscale='Viridis'))],

		
        layout=go.layout.Scene(
            xaxis=dict(range=[-axisD, axisD], autorange=False, zeroline=False),
            yaxis=dict(range=[-axisD, axisD], autorange=False, zeroline=False),
            title_text="Kinematic Generation of a Planar Curve", hovermode="closest",
            updatemenus=[dict(type="buttons",
                              buttons=[dict(label="Play",
                                            method="animate",
                                            args=[None])])]),

        frames=[go.Frame(
            # layout=go.layout.scene(
            #     xaxis=dict(range=[-8E4, 8E4], autorange=False, zeroline=False),
            #     yaxis=dict(range=[-8E4, 8E4], autorange=False, zeroline=False),
            #     zaxis=dict(range=[-8E4, 8E4], autorange=False, zeroline=False)
            # ),
            data=[
                go.Scatter3d(
                    x=[data1[k, 0]],
                    y=[data1[k, 1]],
                    z=[data1[k, 2]],
                    mode="markers",
                    marker=dict(color="red", size=10)),
                go.Scatter3d(
                    x=[data2[k, 0]],
                    y=[data2[k, 1]],
                    z=[data2[k, 2]],
                    mode="markers",
                    marker=dict(color="red", size=10))

            ])for k in range(len(data1))])
    # fig = px.scatter_3d(df, x='x', y='y', z='z', opacity = 0.5, size_max = 5)

    ##########
    # fig.update_layout(
    #     scene=dict(
    #         xaxis=dict(nticks=4, range=[-100, 100],),
    #         yaxis=dict(nticks=4, range=[-50, 100],),
    #         zaxis=dict(nticks=4, range=[-100, 100],),),
    #     width=700,
    #     margin=dict(r=20, l=10, b=10, t=10))
    ###########

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

    plot_data(load("envisat"), load("globalstar"), np.array([[0., 0., 0.]]))
