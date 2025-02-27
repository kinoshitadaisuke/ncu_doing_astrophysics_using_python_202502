#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:18:09 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) of 5x5 shape
# with all the elements initialised by one.
array_o = numpy.ones ( (5, 5) )

# printing Numpy array
print (f'array_o:\n{array_o}')

# printing information
print (f'information:')
print (f'  ndim     = {array_o.ndim}')
print (f'  size     = {array_o.size}')
print (f'  shape    = {array_o.shape}')
print (f'  dtype    = {array_o.dtype}')
print (f'  itemsize = {array_o.itemsize} byte')
