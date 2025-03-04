#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 21:44:37 (CST) daisuke>
#

# importing Numpy module
import numpy

# input data file
file_input = 'numpy_04.npz'

# loading Numpy arrays from npy file
arrays = numpy.load (file_input)

# printing "arrays"
print (f'{arrays}')

# printing object type of "arrays"
print (f'{type (arrays)}')

# first Numpy array in "arrays"
array_c = arrays['array_c']

# second Numpy array in "arrays"
array_d = arrays['array_d']

# printing array_c and array_d
print (f'array_c:')
print (array_c)
print (f'array_d:')
print (array_d)
