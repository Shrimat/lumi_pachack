import numpy as np
import json
import pandas as pd


def load(satellite):
	# Location of the data on disk
	data_path = "data/"

	# path to Envisat orbital data.
	envisat_orbit_path = f'Lumi Space/data/{satellite}_state.json'

	# load the data from file into orbit dictionary
	with open(envisat_orbit_path, 'r') as f:
		orbit = json.load(f)

	# Convert all orbital data to numpy arrays for easier plotting.
	for key in orbit.keys():
		orbit[key] = np.array(orbit[key])

	pos = orbit['pos'][0::100]
	df = pd.DataFrame(pos, columns = ['x','y',"z"])
	
	return df