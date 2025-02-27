#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:37:24 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays (2x2 matrix)
A = numpy.array ([ [1.0, 2.0], [3.0, 4.0] ])
B = numpy.array ([ [4.0, 2.0], [1.0, 3.0] ])

# printing A and B
print (f'A:\n{A}')
print (f'B:\n{B}')

# matrix product
C = A.dot (B)

# printing C
print (f'C = A.dot (B):\n{C}')
