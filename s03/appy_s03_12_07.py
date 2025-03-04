#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 21:05:03 (CST) daisuke>
#

# importing Numpy module
import numpy

# making a Numpy array
data = numpy.array ([
    [9.8, 7.6],
    [5.4, 3.2],
    [1.0, -1.2],
    [-3.4, -5.6],
    [-7.8, -9.0],
])

# printing Numpy array
print (f'{data}')

# output data file
file_output = 'numpy_02.data'

# saving Numpy array into file
numpy.savetxt (file_output, data, fmt='%8.3f',
               header='test data created by numpy.savetxt ()')
