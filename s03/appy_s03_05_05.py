#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:30:25 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
a = numpy.linspace (0.0, 10.0, 11)

# printing a
print (f'a = {a}')

# calculation
# no need of using "for"
b = numpy.sqrt (a)

# printing b
print (f'b = sqrt (a)\n  = {b}')
