#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 14:03:19 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.linspace (0.0, 10.0, 11)

# printing "a"
print (f'a:\n{a}')

# trying a.copy ()
b = a.copy ()

# printing "b"
print (f'b:\n{b}')

# IDs of "a" and "b"
print (f'id (a) = {id (a)}')
print (f'id (b) = {id (b)}')

# changing "a[5]"
a[5] += 10

# printing "a"
print (f'a:\n{a}')

# printing "b"
print (f'b:\n{b}')

# IDs of "a" and "b"
print (f'id (a) = {id (a)}')
print (f'id (b) = {id (b)}')
