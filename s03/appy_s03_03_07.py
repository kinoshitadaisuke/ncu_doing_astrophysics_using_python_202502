#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:22:11 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.linspace ()
array_r = numpy.linspace (1000, 2000, 21)

# printing Numpy array
print (f'array_r:\n{array_r}')

# printing information
print (f'information:')
print (f'  ndim     = {array_r.ndim}')
print (f'  size     = {array_r.size}')
print (f'  shape    = {array_r.shape}')
print (f'  dtype    = {array_r.dtype}')
print (f'  itemsize = {array_r.itemsize} byte')
