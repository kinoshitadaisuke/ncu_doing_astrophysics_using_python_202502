#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 13:29:28 (CST) daisuke>
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
