import numpy as np
import warnings
import os

def extract_data(filename,N,y):
	"""
	Extracts independent and dependent variable values from text file. 
	N-1 independent variables, 1 dependent variable.

	Parameters:
		-filename: str
			name of text file that contains the data
		-N: int
			number of columns of data, both independent and dependent values
		-y: int
			index of column containing dependent value

	Returns:
		-indep: ndarray
			independent variable values stored in 2D array: data point on axis 0, independent variable on axis 1
		-dep: ndarray
			dependent variable values stored in 1D array: data point on axis 0

	Notes:
	Assumes N represents the total number of data columns available--will throw warning if not.
	"""
	assert os.path.isfile(filename), f'No such file/directory "{filename}" exists.' # check if file exists
	assert os.stat(filename).st_size > 0, 'File is empty.' # check if file is empty

	infile = open(filename,'rt')

	# extract data from file
	raw_data = []
	for line in infile:
		raw_data.append(line.rstrip())

	# determine delimiter
	delim = delimiter_check(raw_data[0])

	# clean data
	clean_data = []
	for line in raw_data:
		clean_line = []
		for item in line.split(delim):
			try:
				clean_line.append(float(item))
			except ValueError:
				pass
		if len(clean_line) == N:
			clean_data.append(clean_line)
		elif len(clean_line) > N:
			warnings.warn('Line encountered with more than N columns of data--this line will be ignored.')

	# split independent and dependent variables into separate numpy arrays
	if clean_data:
		clean_data = np.stack(clean_data,axis=0)

		y_ind = y-1 # start count at zero
		dep = clean_data[:,y_ind]
		indep = np.delete(clean_data,y_ind,axis=1)
	else:
		raise ValueError('No usable data found--no rows contain at least N numbers.') 

	return indep, dep

def delimiter_check(line):
	"""
	Determines what delimiter is used in given text file.

	Parameters:
		-line: str
			line from text file

	Returns:
		-delim: str
			delimiter used in text file

	Notes:
	Recognizes only ",", "\t", and ":" delimiters.
	"""
	if ',' in line:
		delim = ','
	elif '\t' in line:
		delim = '\t'
	elif ':' in line:
		delim = ':'
	else:
		raise ValueError('Unrecognized delimiter, use ",", "\t", or ":" instead.')

	return delim