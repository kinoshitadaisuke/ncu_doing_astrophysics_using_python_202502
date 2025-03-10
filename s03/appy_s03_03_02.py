#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:39:55 (CST) daisuke>
#

# importing numpy module
import numpy

# making a 3-dim Numpy array (ndarray) with elements all equal to zeros
array_m = numpy.zeros ( (3, 3, 3) )

# printing Numpy array
print (f'array_m:\n{array_m}')

# printing information
print (f'information:')
print (f'  ndim     = {array_m.ndim}')
print (f'  size     = {array_m.size}')
print (f'  shape    = {array_m.shape}')
print (f'  dtype    = {array_m.dtype}')
print (f'  itemsize = {array_m.itemsize} byte')
