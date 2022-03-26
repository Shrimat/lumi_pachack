import numpy as np
import json
import glob
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


def load(satellite):
	# Location of the data on disk
	data_path = "data/"

	# path to Envisat orbital data.
	envisat_orbit_path = f'data/{satellite}_state.json'

	# load the data from file into orbit dictionary
	with open(envisat_orbit_path, 'r') as f:
		orbit = json.load(f)

	# Convert all orbital data to numpy arrays for easier plotting.
	for key in orbit.keys():
		orbit[key] = np.array(orbit[key])

	pos = orbit['pos'][0::50]
	return pos
	# df = pd.DataFrame(pos, columns = ['x','y',"z"])
	# return df

if __name__ == "__main__":
	load("envisat")

"""
        frames=[go.Frame(
            data=[
                go.Scatter3d(
                    x=[data1[k, 0]],
                    y=[data1[k, 1]],
                    z=[data1[k, 2]],
                    mode="markers",
                    name="Envisat",
                    marker=dict(color="red", size=2)),
                go.Scatter3d(
                    x=[data2[k, 0]],
                    y=[data2[k, 1]],
                    z=[data2[k, 2]],
                    mode="markers",
                    name="Globalstar",
                    marker=dict(color="green", size=2)),
                go.Scatter3d(
                    x=[data3[0, 0]],
                    y=[data3[0, 1]],
                    z=[data3[0, 2]],
                    mode="markers",
                    name="Earth",
                    marker=dict(color="blue", size=20)),
                go.Scatter3d(
                    x=[data1[max(k-200, 0):k+1, 0]],
                    y=[data1[max(k-200, 0):k+1, 1]],
                    z=[data1[max(k-200, 0):k+1, 2]],
                    mode="lines",
                    line=dict(color="red", width=5)),
                go.Scatter3d(
                    x=[data2[max(k-200, 0):k+1, 0]],
                    y=[data2[max(k-200, 0):k+1, 1]],
                    z=[data2[max(k-200, 0):k+1, 2]],
                    mode="lines",
                    line=dict(color="green", width=5)),
            ],
            layout={
                "xaxis": {"range": [-axisScale * Re, axisScale * Re]},
                "yaxis": {"range": [-axisScale * Re, axisScale * Re]}
            }
            )for k in range(len(data1))])
"""