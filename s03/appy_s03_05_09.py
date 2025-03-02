#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 13:38:41 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays
a = numpy.array ([1.0, 2.0])
b = numpy.array ([3.0, 4.0])

# printing a and b
print (f'a                  = {a}')
print (f'b                  = {b}')

# dot product of two vectors
dot = numpy.dot (a, b)

# printing dot product
print (f'numpy.dot (a, b)   = {dot}')

# inner product of two vectors
inner = numpy.inner (a, b)

# printing inner product
print (f'numpy.inner (a, b) = {inner}')

# confirmation
print (f'a0 x b0 + a1 x b1  = {a[0]*b[0]+a[1]*b[1]}')
