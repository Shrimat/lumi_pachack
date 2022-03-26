from dash import Dash, html, dcc
from test_3d import plot_data
from load_data import load

app = Dash(__name__)

fig = plot_data(load("envisat"), load("globalstar"))

app.layout = html.Div(children=[
    html.H1(children='Lumi Satellite Orbital Data'),

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
