#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 13:42:05 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array (2x2 matrix)
A = numpy.array ([ [1.0, 2.0], [3.0, 4.0] ])

# printing A
print (f'A:\n{A}')

# making Numpy array (2x2 unit matrix)
E2 = numpy.identity (2)

# printing E2
print (f'E2:\n{E2}')

# calculation
B = A @ E2

# printing B
print (f'B = A @ E2:\n{B}')
