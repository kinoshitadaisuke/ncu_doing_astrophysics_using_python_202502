#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 13:39:36 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays
a = numpy.array ([1.0, 1.0, 0.0])
b = numpy.array ([-1.0, 3.0, 0.0])

# printing a and b
print (f'a     = {a}')
print (f'b     = {b}')

# dot product of two vectors
dot = numpy.dot (a, b)

# printing dot product
print (f'dot   = {dot}')

# inner product of two vectors
inner = numpy.inner (a, b)

# printing inner product
print (f'inner = {inner}')

# cross product of two vectors
cross = numpy.cross (a, b)

# printing cross product
print (f'cross = {cross}')
