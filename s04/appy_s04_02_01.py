#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/07 15:46:37 (CST) daisuke>
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
parser = argparse.ArgumentParser (description='changing line style')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output    = args.output
resolution_dpi = args.resolution

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# check of extension of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing a message
    print (f'ERROR: output file must be either EPS or PDF or PNG or PS file.')
    # stopping the script
    sys.exit (0)

# data to be plotted
data_x  = numpy.linspace (-10.0, +10.0, 10**3)
data_c0 = numpy.sin (data_x)
data_c1 = numpy.sin (data_x - numpy.pi / 4.0)
data_c2 = numpy.sin (data_x - numpy.pi / 2.0)
data_c3 = numpy.sin (data_x - numpy.pi * 3.0 / 4.0)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_c0, color='k', linestyle='-',  label='solid line')
ax.plot (data_x, data_c1, color='k', linestyle='--', label='dashed line')
ax.plot (data_x, data_c2, color='k', linestyle='-.', label='dash-dotted line')
ax.plot (data_x, data_c3, color='k', linestyle=':',  label='dotted line')

# setting ranges of x-axis and y-axis
ax.set_xlim (-10.0, +10.0)
ax.set_ylim (-1.2, +1.9)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (-10.0, +10.0, 11))
ax.set_yticks (numpy.linspace (-1.0, +1.0, 5))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output, dpi=resolution_dpi)
