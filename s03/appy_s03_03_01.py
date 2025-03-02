#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:39:36 (CST) daisuke>
#

# importing numpy module
import numpy

# making a 2-dim Numpy array (ndarray) with elements all equal to zeros
array_l = numpy.zeros ( (5, 5) )

# printing Numpy array
print (f'array_l:\n{array_l}')

# printing information
print (f'information:')
print (f'  ndim     = {array_l.ndim}')
print (f'  size     = {array_l.size}')
print (f'  shape    = {array_l.shape}')
print (f'  dtype    = {array_l.dtype}')
print (f'  itemsize = {array_l.itemsize} byte')
