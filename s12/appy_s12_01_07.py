#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/19 12:55:14 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'appy_s12_01_00.data'

# output file name
file_output = 'appy_s12_01_07.png'

# best fit period (day)
p_best = 7.4981 / 24.0

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
data_phase = numpy.array ([])
data_mag   = numpy.array ([])
data_err   = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (datetime, mjd_str, mag_str, err_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        err = float (err_str)
        phase = mjd / p_best - int (mjd / p_best)
        # appending the data at the end of numpy arrays
        data_mjd   = numpy.append (data_mjd, mjd)
        data_phase = numpy.append (data_phase, phase)
        data_mag   = numpy.append (data_mag, mag)
        data_err   = numpy.append (data_err, err)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Phase')
ax.set_ylabel ('Apparent Magnitude [mag]')

# axes
ax.invert_yaxis ()

# plotting data
ax.errorbar (data_phase, data_mag, yerr=data_err, \
             linestyle='None', marker='o', markersize=5, color='blue', \
             ecolor='black', capsize=5, \
             label='folded lightcurve')
ax.errorbar (data_phase + 1, data_mag, yerr=data_err, \
             linestyle='None', marker='o', markersize=5, color='blue', \
             ecolor='black', capsize=5)
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=150)
