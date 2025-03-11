#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/10 22:46:52 (CST) daisuke>
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
descr  = f'Making a pie chart'
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
list_type     = []
list_fraction = []
    
# opening input data file
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if the line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting the line
        (type_str, fraction_str) = line.split (',')
        # converting string into float
        fraction = float (fraction_str)
        # appending data into lists
        list_type.append (type_str)
        list_fraction.append (fraction)

# making numpy arrays
array_fraction = numpy.array (list_fraction)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a pie chart
ax.pie (array_fraction, labels=list_type, colors=['blue', 'green', 'red'], \
        startangle=90.0, counterclock=False, center=(0,0))

# saving a plot as a file
fig.savefig (file_output, dpi=resolution_dpi)
