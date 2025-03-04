#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 21:28:20 (CST) daisuke>
#

# importing Numpy module
import numpy

# input data file
file_input = 'numpy_03.npy'

# loading a Numpy array from npy file
array_b = numpy.load (file_input)

# printing Numpy array
print (f'{array_b}')

# object type of the object "array_b"
type_array_b = type (array_b)

# printing object type
print (f'object type = {type_array_b}')

# printing information of Numpy array
print (f'information:')
print (f'  ndim     = {array_b.ndim}')
print (f'  size     = {array_b.size}')
print (f'  shape    = {array_b.shape}')
print (f'  dtype    = {array_b.dtype}')
print (f'  itemsize = {array_b.itemsize} byte')
