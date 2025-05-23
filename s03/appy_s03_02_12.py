#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 12:34:47 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) of a specified data type
# float32 : 32-bit floating point number
array_h = numpy.array ([-9.8, -7.6, -5.4, -3.2, -1.0, \
                        1.2, 3.4, 5.6, 7.8, 9.0], \
                       dtype='float32')

# printing Numpy array
print (f'array_h:\n{array_h}')

# printing information
print (f'information:')
print (f'  ndim     = {array_h.ndim}')
print (f'  size     = {array_h.size}')
print (f'  shape    = {array_h.shape}')
print (f'  dtype    = {array_h.dtype}')
print (f'  itemsize = {array_h.itemsize} byte')
