from dash import Dash, html, dcc
from test_3d import plot_data
from load_data import load
import dash_bootstrap_components as dbc

app = Dash(__name__)

fig = plot_data(load("envisat"), load("globalstar"))

app.layout = html.Div(children=[
    dbc.Row(dbc.Col(html.H1(children='Lumi Satellite Orbital Data'), width=6)),
    html.Div(children='''
        Orbits for Envisat and Globalstar satellites
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
