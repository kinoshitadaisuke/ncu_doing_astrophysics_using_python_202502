#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:24:26 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.linspace ()
array_t = numpy.linspace (0, 10, 11)

# printing Numpy array
print (f'array_t:\n{array_t}')

# printing information
print (f'information:')
print (f'  ndim     = {array_t.ndim}')
print (f'  size     = {array_t.size}')
print (f'  shape    = {array_t.shape}')
print (f'  dtype    = {array_t.dtype}')
print (f'  itemsize = {array_t.itemsize} byte')

# appending one more data to "array_t"
array_t = numpy.append (array_t, 11.0)

# printing Numpy array
print (f'array_t:\n{array_t}')

# printing information
print (f'information:')
print (f'  ndim     = {array_t.ndim}')
print (f'  size     = {array_t.size}')
print (f'  shape    = {array_t.shape}')
print (f'  dtype    = {array_t.dtype}')
print (f'  itemsize = {array_t.itemsize} byte')
