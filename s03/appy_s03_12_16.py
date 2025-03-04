#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 21:54:31 (CST) daisuke>
#

# importing Numpy module
import numpy

# input data file
file_input = 'numpy_05.npz'

# loading Numpy arrays from npy file
arrays = numpy.load (file_input)

# printing "arrays"
print (f'{arrays}')

# printing object type of "arrays"
print (f'{type (arrays)}')

# first Numpy array in "arrays"
array_e = arrays['array_e']

# second Numpy array in "arrays"
array_f = arrays['array_f']

# third Numpy array in "arrays"
array_g = arrays['array_g']

# printing array_c and array_d
print (f'array_e:')
print (array_e)
print (f'array_f:')
print (array_f)
print (f'array_g:')
print (array_g)
