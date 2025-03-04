#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 21:53:02 (CST) daisuke>
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
