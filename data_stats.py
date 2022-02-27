#!/usr/bin/env python3

import argparse
from data_read import extract_data
import minmax
import average
import ratio

parser  = argparse.ArgumentParser(description='Reads a file containing data, and outputs statistics of the data')

# mandatory inputs
parser.add_argument('-N',type=int,required=True,
	help='int - specifies the total number of data columns, including y, e.g. -N 5')
parser.add_argument('-y',type=int,required=True,
	help='int - specifies which column (1 to N) contains the dependent variable y, e.g. -y 5')
parser.add_argument('-i',required=True,
	help='str - specifies the name of the data file to be analyzed, e.g. -i "myfile.txt"')

# optional inputs
parser.add_argument('-M',action='store_true',
	help='display min and max of the dependent variable y')
parser.add_argument('-a',action='store_true',
	help='display average and mean square of each column')
parser.add_argument('-s',action='store_true',
	help='display ration between average of each y divided by the average of their respective x variables')

args = parser.parse_args()

def main():
	assert any([args.M,args.a,args.s]), 'At least one of -M, -a, or -s must be used.'
	assert args.N>0, 'Invalid input for N: must be positive integer.'
	assert args.y<=args.N and args.y>0, 'Invalid input for y: must be positive integer <= N.'

	indep, dep = extract_data(args.i,args.N,args.y)

	print('\n')

	if args.M:
		minmax.compute(indep,dep)
	if args.a:
		average.compute(indep,dep)
	if args.s:
		ratio.compute(indep,dep)

if __name__ == "__main__":

	main()