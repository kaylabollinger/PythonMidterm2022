import numpy as np

def compute(indep,dep):
	"""
	Computes/prints the average and mean square of each column.

	Parameters:
		-indep: ndarray
			independent variable values stored in 2D array: data point on axis 0, independent variable on axis 1
		-dep: ndarray
			dependent variable values stored in 1D array: data point on axis 0

	Returns:
		None

	Notes:
	Prints independent and dependent results separately.
	"""
	# compute averages
	avg_indep = np.average(indep,axis=0)
	avg_dep = np.average(dep,axis=0)
	print('Average(s) of:')
	print(f'Independent Variables: {avg_indep}')
	print(f'Dependent Variable: {avg_dep}')
	print('\n')

	# compute mean squares
	msq_indep = np.average(indep**2,axis=0)
	msq_dep = np.average(dep**2,axis=0)
	print('Mean Square(s) of:')
	print(f'Independent Variables: {msq_indep}')
	print(f'Dependent Variable: {msq_dep}')
	print('\n')