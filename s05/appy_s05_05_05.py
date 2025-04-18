#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:23:43 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# function of f(x) = cos (x)
def curve (x):
    # curve
    y = numpy.cos (x)
    # returning a value
    return (y)

# data points
data_x = numpy.linspace (0.0, numpy.pi / 2.0, 1001)
data_y = curve (data_x)

# printing data_x and data_y
print (f'data_x = {data_x}')
print (f'data_y = {data_y}')

# numerical integration of given data points by trapezoidal rule
I = scipy.integrate.trapezoid (data_y, x=data_x)

# printing result of numerical integration
print (f'I = {I}')
