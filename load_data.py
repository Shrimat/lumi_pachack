import numpy as np
import json
import glob
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from test_3d import plot_data


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

	pos = orbit['pos'][0::100]
	df = pd.DataFrame(pos, columns = ['x','y',"z"])
	
	return df

if __name__ == "__main__":
	plot_data(load("envisat"))