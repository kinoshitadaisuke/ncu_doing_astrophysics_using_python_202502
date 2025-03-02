#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:53:11 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.logspace ()
array_s = numpy.logspace (0, 5, 11)

# printing Numpy array
print (f'array_s:\n{array_s}')

# printing information
print (f'information:')
print (f'  ndim     = {array_s.ndim}')
print (f'  size     = {array_s.size}')
print (f'  shape    = {array_s.shape}')
print (f'  dtype    = {array_s.dtype}')
print (f'  itemsize = {array_s.itemsize} byte')
