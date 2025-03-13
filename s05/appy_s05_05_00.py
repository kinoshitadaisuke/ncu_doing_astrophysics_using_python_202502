#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:22:32 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# function of a curve
def curve (x):
    # curve
    y = numpy.sin (x)
    # returning a value
    return (y)

# range of integration
x0 = 0.0
x1 = numpy.pi

# numerical integration
result = scipy.integrate.quad (curve, x0, x1)

# printing result of numerical integration
print (f'integ. of sin (x) from 0.0 to pi = {result[0]} +/- {result[1]}')
