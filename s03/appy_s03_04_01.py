#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:26:21 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
array_u = numpy.linspace (0, 10, 11)
array_v = numpy.linspace (11, 15, 9)

# printing Numpy array
print (f'array_u:\n{array_u}')

# printing information
print (f'information:')
print (f'  ndim     = {array_u.ndim}')
print (f'  size     = {array_u.size}')
print (f'  shape    = {array_u.shape}')
print (f'  dtype    = {array_u.dtype}')
print (f'  itemsize = {array_u.itemsize} byte')

# printing Numpy array
print (f'array_v:\n{array_v}')

# printing information
print (f'information:')
print (f'  ndim     = {array_v.ndim}')
print (f'  size     = {array_v.size}')
print (f'  shape    = {array_v.shape}')
print (f'  dtype    = {array_v.dtype}')
print (f'  itemsize = {array_v.itemsize} byte')

# concatenating array_u and array_v, and creating array_w
array_w = numpy.concatenate ([array_u, array_v])

# printing Numpy array
print (f'array_w:\n{array_w}')

# printing information
print (f'information:')
print (f'  ndim     = {array_w.ndim}')
print (f'  size     = {array_w.size}')
print (f'  shape    = {array_w.shape}')
print (f'  dtype    = {array_w.dtype}')
print (f'  itemsize = {array_w.itemsize} byte')
