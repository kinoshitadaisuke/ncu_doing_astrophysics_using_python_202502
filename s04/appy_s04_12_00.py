#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/10 08:39:57 (CST) daisuke>
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
descr  = f'A sample polar plot using Matplotlib'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('radius', nargs='+', type=float, default='', \
                     help='radii of circles')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output    = args.output
resolution_dpi = args.resolution
list_radius    = args.radius

# if "file_output" is empty, then stop the script
if (file_output == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: need to specify output file name!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# making pathlib object
path_output = pathlib.Path (file_output)

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: output file "{file_output}" already exists!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='polar')

# number of data points
n = 10000

# coordinate settings
ax.set_rlim (0.0, numpy.amax (list_radius) * 1.2)
ax.grid (True)

# for each radius
for r in list_radius:
    # r
    array_radius = numpy.array ([r] * n)
    # theta
    array_theta = numpy.linspace (0.0, 2.0 * numpy.pi, n)
    # plotting a circle
    ax.plot (array_theta, array_radius, linestyle='-', label=f'radius {r}')

# legend
a = 45.0
legend_x = 0.5 * numpy.cos (a) + 0.5
legend_y = 0.5 * numpy.sin (a) + 0.5
ax.legend (loc='lower left', bbox_to_anchor=(legend_x, legend_y))

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)
