#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:29:10 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
a = numpy.linspace (4.0, 40.0, 10)
b = numpy.linspace (2.0, 20.0, 10)

# printing a and b
print (f'a = {a}')
print (f'b = {b}')

# calculation
# no need of using "for"
c = a / b

# printing c
print (f'c = a / b = {c}')
