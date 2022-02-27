import numpy as np

def compute(indep,dep):
	"""
	Computes/prints the ratio of the average of the dependent variable 
	divided by the average of each of the independent variables.

	Parameters:
		-indep: ndarray
			independent variable values stored in 2D array: data point on axis 0, independent variable on axis 1
		-dep: ndarray
			dependent variable values stored in 1D array: data point on axis 0

	Returns:
		None

	Notes:
	None.
	"""
	# compute averages
	avg_indep = np.average(indep,axis=0)
	avg_dep = np.average(dep,axis=0)

	print(f'Ratio of averages: {avg_dep/avg_indep}')
	print('\n')