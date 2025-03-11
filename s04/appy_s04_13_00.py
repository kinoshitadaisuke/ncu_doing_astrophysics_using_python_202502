#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/10 21:43:11 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
descr  = f'Making a plot using .fill_between () method'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', default='', \
                     help='input file name')
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_input     = args.input
file_output    = args.output
resolution_dpi = args.resolution

# if "file_input" is empty, then stop the script
if (file_input == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: need to specify input file name!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# if "file_output" is empty, then stop the script
if (file_output == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: need to specify output file name!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# making pathlib object
path_input  = pathlib.Path (file_input)
path_output = pathlib.Path (file_output)

# existence check of input file
if not (path_input.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: input file "{file_input}" does not exist!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: output file "{file_output}" already exists!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# making empty lists for storing data
list_year   = []
list_t_mean = []
list_t_high = []
list_t_low  = []
    
# opening input data file
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if the line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting the line
        (year_str, t_mean_str, t_high_str, t_low_str) = line.split ()
        # converting string into int/float
        year   = int (year_str)
        t_mean = float (t_mean_str)
        t_high = float (t_high_str)
        t_low  = float (t_low_str)
        # appending data into lists
        list_year.append (year)
        list_t_mean.append (t_mean)
        list_t_high.append (t_high)
        list_t_low.append (t_low)

# making numpy arrays
array_year   = numpy.array (list_year)
array_t_mean = numpy.array (list_t_mean)
array_t_high = numpy.array (list_t_high)
array_t_low  = numpy.array (list_t_low)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# plotting daily mean temperature
ax.fill_between (array_year, array_t_low, array_t_high, alpha=0.5, linewidth=0)
ax.plot (array_year, array_t_mean, linestyle='-', linewidth=3, color='blue', \
         label='daily mean temperature in Tokyo')

# axes
ax.grid ()
ax.set_xlabel ('Year')
ax.set_ylabel ('Temperature [deg C]')

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output, dpi=resolution_dpi)
