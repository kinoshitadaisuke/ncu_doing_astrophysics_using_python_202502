#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/16 12:02:45 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# parameters
a           = 5.0
b           = 3.0
xerr_mean   = 0.5
xerr_stddev = 0.2
yerr_mean   = 3.0
yerr_stddev = 0.8
x_min       = -10.0
x_max       = +10.0
n_data      = 21
file_output = 'appy_s05_10_00.data'

# function for generating data
def func (x, a, b):
    y = a * x + b
    return (y)

# random number generator
rng = numpy.random.default_rng ()

# generating synthetic data
x = numpy.linspace (x_min, x_max, n_data) \
    + numpy.absolute (
        rng.normal (loc=xerr_mean, scale=xerr_stddev, size=n_data) )
x_err = numpy.absolute (
    rng.normal (loc=xerr_mean, scale=xerr_stddev, size=n_data) )
y = func (numpy.linspace (x_min, x_max, n_data), a, b) \
    + numpy.absolute (
        rng.normal (loc=yerr_mean, scale=yerr_stddev, size=n_data) )
y_err = numpy.absolute (
    rng.normal (loc=yerr_mean, scale=yerr_stddev, size=n_data) )

# writing generated synthetic data to a file
with open (file_output, 'w') as fh_w:
    fh_w.write (f'#\n')
    fh_w.write (f'# synthetic data for fitting using ODR\n')
    fh_w.write (f'#\n')
    fh_w.write (f'#  format of this data file:\n')
    fh_w.write (f'#    1st column : x\n')
    fh_w.write (f'#    2nd column : x_err\n')
    fh_w.write (f'#    3rd column : y\n')
    fh_w.write (f'#    4th column : y_err\n')
    fh_w.write (f'#\n')
    for i in range (len (x)):
        fh_w.write (f'{x[i]:8.3f} {x_err[i]:8.3f} {y[i]:8.3f} {y_err[i]:8.3f}\n')
