import numpy as np
import json


def load(satellite):
	# path to Envisat orbital data.
	envisat_orbit_path = f'Lumi Space/data/{satellite}_state.json'

	# load the data from file into orbit dictionary
	with open(envisat_orbit_path, 'r') as f:
		orbit = json.load(f)

	# Convert all orbital data to numpy arrays for easier plotting.
	for key in orbit.keys():
		orbit[key] = np.array(orbit[key])

	pos = orbit['pos'][0::50]
	if satellite == "globalstar":
		extra = (orbit["time"][0] - 631154907) // 50
		pos = np.append(np.array([[None, None, None] for i in range(extra)]), pos, axis=0)
	return pos