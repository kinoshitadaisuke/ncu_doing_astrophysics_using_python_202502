#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 21:55:19 (CST) daisuke>
#

# importing Numpy module
import numpy

# output file name
file_output = 'numpy_05.npz'

# lists
list_e = [ 1.2, 3.4, 5.6 ]
list_f = [
    [-10.0, 0.0],
    [10.0, 20.0],
]
list_g = [
    [-400.0, -300.0, -200.0],
    [-100.0, 0.0, 100.0],
    [200.0, 300.0, 400.0],
]

# making Numpy arrays from lists
array_e = numpy.array (list_e)
array_f = numpy.array (list_f)
array_g = numpy.array (list_g)

# printing Numpy arrays
print (f'array_e:')
print (f'{array_e}')
print (f'array_f:')
print (f'{array_f}')
print (f'array_g:')
print (f'{array_g}')

# saving Numpy array into compressed "npz" file
numpy.savez_compressed (file_output,
                        array_e=array_e, array_f=array_f, array_g=array_g)
