#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/04 11:11:59 (UT+08:00) daisuke>
#

# importing numpy
import numpy

# output file name
file_output = 'synthetic_00.data'

# parameters
x_min  = 0.0
x_max  = 50.0
n_data = 30
a      = 2.0
b      = 3.0

# random number generator
rng = numpy.random.default_rng ()

# function y=a*x+b
def func (a, b, x):
    y = a * x + b
    return (y)

# generation of data
data_x = rng.uniform (x_min, x_max, n_data)
data_y = func (a, b, data_x) + rng.normal (loc=0.0, scale=0.5, size=n_data)
data   = numpy.array ([data_x, data_y]).T

# writing data to file
with open (file_output, 'w') as fh_w:
    for (x, y) in data:
        fh_w.write (f'{x:8.3f} {y:8.3f}\n')
