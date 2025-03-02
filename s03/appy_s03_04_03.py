#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:55:52 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array
a = numpy.array ([ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ])

# printing Numpy array "a"
print (f'a:')
print (f'{a}')

# flattening of a Numpy array
b = a.flatten ()

# printing Numpy array "b"
print (f'b:')
print (f'{b}')
