#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:43:04 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with 100 elements all equal to ones.
array_n = numpy.ones ( (100,) )

# printing Numpy array
print (f'array_n:\n{array_n}')

# printing information
print (f'information:')
print (f'  ndim     = {array_n.ndim}')
print (f'  size     = {array_n.size}')
print (f'  shape    = {array_n.shape}')
print (f'  dtype    = {array_n.dtype}')
print (f'  itemsize = {array_n.itemsize} byte')
