#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/04 11:20:27 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# input file name
file_input = 'synthetic_00.data'

# output file name
file_output = 'appy_s07_07_01.png'

# making empty lists for storing data
list_x = []
list_y = []

# opening file for reading
with open (file_input, 'r') as fh_r:
    # reading file line-by-line
    for line in fh_r:
        # skipping line if line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (x_str, y_str) = line.split ()
        # converting string into float
        try:
            x = float (x_str)
        except:
            continue
        try:
            y = float (y_str)
        except:
            continue
        # appending extracted data to the end of lists
        list_x.append (x)
        list_y.append (y)

# making numpy arrays
array_x = numpy.array (list_x)
array_y = numpy.array (list_y)

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# plotting data
ax.plot (array_x, array_y, \
         linestyle='None', marker='o', markersize=3, color='blue', \
         label='synthetic data points')

# settings for axes
ax.legend ()
ax.grid ()
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# saving plot into a file
fig.savefig (file_output, dpi=150)
