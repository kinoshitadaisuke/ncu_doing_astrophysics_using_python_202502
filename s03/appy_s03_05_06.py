#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:30:46 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.logspace ()
a = numpy.logspace (-5.0, 5.0, 11)

# printing a
print (f'a = {a}')

# calculation
# no need of using "for"
b = numpy.log10 (a)

# printing b
print (f'b = log10 (a) = {b}')
