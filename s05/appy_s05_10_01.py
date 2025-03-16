#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/16 12:15:00 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# input data file name
file_input = 'appy_s05_10_00.data'

# output image file name
file_output = 'appy_s05_10_01.png'

# resolution in DPI
resolution_dpi = 150

# making empty lists for storing data
list_x     = []
list_x_err = []
list_y     = []
list_y_err = []

# opening data file for reading
with open (file_input, 'r') as fh_r:
    # reading file line-by-line
    for line in fh_r:
        # skip if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting data
        (x_str, x_err_str, y_str, y_err_str) = line.split ()
        # converting string into float
        x     = float (x_str)
        x_err = float (x_err_str)
        y     = float (y_str)
        y_err = float (y_err_str)
        # appending data to the end of lists
        list_x.append (x)
        list_x_err.append (x_err)
        list_y.append (y)
        list_y_err.append (y_err)

# making numpy arrays
array_x    = numpy.array (list_x)
array_xerr = numpy.array (list_x_err)
array_y    = numpy.array (list_y)
array_yerr = numpy.array (list_y_err)

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')
ax.set_xlim (-12.0, +12.0)
ax.set_ylim (-65.0, +65.0)

# plotting data
ax.errorbar (array_x, array_y, xerr=array_xerr, yerr=array_yerr, \
             linestyle='None', marker='o', markersize=5, color='blue', \
             ecolor='black', elinewidth=2, capsize=3, \
             label='synthetic data for ODR')

# legend
ax.legend ()

# saving plot into file
fig.savefig (file_output, dpi=resolution_dpi)
