import numpy as np
import json


def load_pass(satellite, station):
	# path to Envisat orbital data.
	passes_path = f'Lumi Space/data/{satellite}_passes.json'

	if station == "graz":
		indx = 0
	elif station == "herstmonceux":
		indx = 1
	else:
		raise ValueError("Station must be \"graz\" or \"herstmonceux\"")

	# load the data from file into orbit dictionary
	with open(passes_path, 'r') as f:
		groundstations = json.load(f)

	# convert to numpy arrays for easier plotting
	for groundstation in groundstations:
		for gs_pass in groundstation['passes']:
			for key in gs_pass.keys():
				if type(gs_pass[key]):
					gs_pass[key] = np.array(gs_pass[key])

	A = np.array([])
	E = np.array([])
	T = np.array([])
	for pass_idx in range(1, 8):
		azimuth = groundstations[indx]['passes'][pass_idx]["azimuth"][::50]*(180.0/np.pi)
		elevation = 90-groundstations[indx]['passes'][pass_idx]["elevation"][::50]*(180.0/np.pi)
		time = groundstations[indx]["passes"][pass_idx]["time"][::50]

		if pass_idx != 7:
			old_t = int(time[-1])
			next_t = int(groundstations[indx]["passes"][pass_idx + 1]["time"][0])
			diff = (next_t-old_t)//50-1
			azimuth = np.append(azimuth, np.array([None for i in range(diff)]))
			elevation = np.append(elevation, np.array([None for i in range(diff)]))
			time = np.append(time, np.array([None for i in range(diff)]))

		A = np.append(A, azimuth)
		E = np.append(E, elevation)
		T = np.append(T, time)

	t0 = 631154907
	t1 = 631241306
	# T[0] = 631167819
	# T[-1] = 631221123
	before = (int(T[0]) - t0)//50
	after = (t1 - int(T[-1]))//50

	A = np.append(np.array([None for i in range(before)]), A)
	A = np.append(A, np.array([None for i in range(after)]))
	E = np.append(np.array([None for i in range(before)]), E)
	E = np.append(E, np.array([None for i in range(after)]))
	T = np.arange(t0, t1 + 1, 50)[:A.shape[0]]
	A = A[:T.shape[0]]
	E = E[:T.shape[0]]

	return np.column_stack((A, E, T))

