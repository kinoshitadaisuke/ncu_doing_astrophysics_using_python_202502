#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/05 11:20:08 (UT+08:00) daisuke>
#

# importing numpy
import numpy

# output file name
file_output = 'synthetic_01.data'

# parameters
x0_min    = 0.0
x0_max    = 10.0
x1_min    = 10.0
x1_max    = 40.0
x2_min    = 40.0
x2_max    = 50.0
y0_offset = -5.0
y1_offset = +0.0
y2_offset = +5.0
n0_data   = 10
n1_data   = 20
n2_data   = 10
a         = 2.0
b         = 3.0

# random number generator
rng = numpy.random.default_rng ()

# function y=a*x+b
def func (a, b, x):
    y = a * x + b
    return (y)

# generation of data
data_x0    = rng.uniform (x0_min, x0_max, n0_data)
data_y0    = func (a, b, data_x0) + y0_offset \
    + rng.normal (loc=0.0, scale=0.5, size=n0_data)
data_yerr0 = numpy.absolute (rng.normal (loc=0.0, scale=0.5, size=n0_data) ) \
    + numpy.absolute (y0_offset)
data_x1    = rng.uniform (x1_min, x1_max, n1_data)
data_y1    = func (a, b, data_x1) + y1_offset \
    + rng.normal (loc=0.0, scale=0.5, size=n1_data)
data_yerr1 = numpy.absolute (rng.normal (loc=0.0, scale=0.5, size=n1_data) ) \
    + numpy.absolute (y1_offset)
data_x2    = rng.uniform (x2_min, x2_max, n2_data)
data_y2    = func (a, b, data_x2) + y2_offset \
    + rng.normal (loc=0.0, scale=0.5, size=n2_data)
data_yerr2 = numpy.absolute (rng.normal (loc=0.0, scale=0.5, size=n2_data) ) \
    + numpy.absolute (y2_offset)
data_x     = numpy.concatenate ([data_x0, data_x1, data_x2])
data_y     = numpy.concatenate ([data_y0, data_y1, data_y2])
data_yerr  = numpy.concatenate ([data_yerr0, data_yerr1, data_yerr2])
data       = numpy.array ([data_x, data_y, data_yerr]).T

# writing data to file
with open (file_output, 'w') as fh_w:
    fh_w.write (f'# x, y, y_err\n')
    for (x, y, y_err) in data:
        fh_w.write (f'{x:8.3f} {y:8.3f} {y_err:8.3f}\n')
