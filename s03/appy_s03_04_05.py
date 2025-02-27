#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 22:40:08 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array
a = numpy.array ([ [1.0, 2.0, 3.0], [100.0, 200.0, 300.0] ])

# printing Numpy array "a"
print (f'a:')
print (f'{a}')

# making a transposed array
b = a.T

# printing Numpy array "b"
print (f'b:')
print (f'{b}')
