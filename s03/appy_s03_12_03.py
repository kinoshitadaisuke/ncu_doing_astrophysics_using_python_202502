#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 20:17:37 (CST) daisuke>
#

# importing Numpy module
import numpy

# input data file
file_input = 'numpy_00.data'

# opening and reading file and storing data in a Numpy array
data = numpy.loadtxt (file_input)

# printing data
print (f'{data}')

# object type of the object "data"
type_data = type (data)

# printing object type
print (f'object type = {type_data}')
