#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:46:10 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.arange ()
array_q = numpy.arange (0, 30, 2)

# printing Numpy array
print (f'array_q:\n{array_q}')

# printing information
print (f'information:')
print (f'  ndim     = {array_q.ndim}')
print (f'  size     = {array_q.size}')
print (f'  shape    = {array_q.shape}')
print (f'  dtype    = {array_q.dtype}')
print (f'  itemsize = {array_q.itemsize} byte')
