# Python Mid Semester Project 2022

Run **data_stats.py** to get statistics of data file--needs python3.

Input: 
- -N : (required, int) number of columns of data (including dependent variable)
- -y : (required, int) index for column containing dependent variable
- -i : (required, str) file name/path for data (.txt)
- -M : (optional) return min/max values of dependent variable
- -a : (optional) return averages of independent and dependent variables
- -s : (optional) return ratio of independent and dependent variables

Example command line use:
python3 data_stats.py -N 10 -y 10 -i 'myfile.txt' -Mas

**NOTE**: at least one of -M, -a, or -s must be used (else data_stats.py does nothing).

*modules*:
- **data_stats.py**: reads a file containing data and outputs statistics of the data.
- **data_read.py**: Extracts and cleans data.
- **minmax.py**: (-M) Computes/prints the (fake) minimum and maximum dependent variable
values.
- **average.py**: (-a) Computes/prints the average and mean square of each column.
- **ratio.py**: (-s) Computes/prints the ratio of the average of the dependent variable
divided by the average of each of the independent variables.

*Contributions.pdf*: file describing team member contributions
*API.pdf*: file describing API used by the modules
