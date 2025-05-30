#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:18:48 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.interpolate

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
descr  = 'carrying out linear interpolation for a curve'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-a', '--coeffa', type=float, default=1.0, \
                     help='coefficient a of curve (default: 1.0)')
parser.add_argument ('-b', '--coeffb', type=float, default=0.0, \
                     help='coefficient b of curve (default: 0.0)')
parser.add_argument ('-c', '--coeffc', type=float, default=0.0, \
                     help='coefficient c of curve (default: 0.0)')
parser.add_argument ('-x', '--xvalue', type=float, default=0.0, \
                     help='X-value of interpolation (default: 0.0)')
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
a              = args.coeffa
b              = args.coeffb
c              = args.coeffc
xi             = args.xvalue
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

# generating data for interpolation
data_x = numpy.linspace (-10.0, 10.0, 11)
data_y = a * (data_x - b)**2 + c

# printing data_x and data_y
print (f'curve: y = {a} * (x - {b})**2 + {c}')
print (f'  data_x = {data_x}')
print (f'  data_y = {data_y}')

# making a function for linear interpolation
func_interp = scipy.interpolate.interp1d (data_x, data_y, kind='linear')

# getting Y-value for X-value at X-value of "xi"
yi = func_interp (xi)

# printing result
print (f'result of interpolation:')
print (f'  func_interp ({xi}) = {yi}')
print (f'what we expect:')
print (f'  x={xi} --> y = {a} * ({xi} - {b})**2 + {c} = {a*(xi-b)**2+c}')

#
# visualisation of result of interpolation using Matplotlib
#

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# plotting data points
ax.plot (data_x, data_y, \
         linestyle='None', marker='o', markersize=8.0, color='blue', \
         zorder=0.1, \
         label='raw data')

# plotting result of interpolation
data_xi = numpy.linspace (-10.0, 10.0, 1001)
data_yi = func_interp (data_xi)
ax.plot (data_xi, data_yi, \
         linestyle=':', linewidth=3.0, color='red', \
         zorder=0.0, \
         label='linear interpolation')

# plotting interpolated values
ax.plot (xi, yi, \
         linestyle='None', marker='^', markersize=10.0, color='cyan', \
         zorder=0.2, \
         label='result of interpolation')

# labels
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)
