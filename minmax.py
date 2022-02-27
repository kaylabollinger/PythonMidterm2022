import numpy as np

def compute(indep,dep):
	"""
	Computes/prints the (fake) minimum and maximum dependent variable values.

	Parameters:
		-indep: ndarray
			independent variable values stored in 2D array: data point on axis 0, independent variable on axis 1
		-dep: ndarray
			dependent variable values stored in 1D array: data point on axis 0

	Returns:
		None

	Notes:
	Prints fake results.
	"""
	fake_results = np.random.rand(2)
	print('Minimum of Dependent Variable: '+str(min(fake_results)))
	print('Maximum of Dependent Variable: '+str(max(fake_results)))
	print('\n')