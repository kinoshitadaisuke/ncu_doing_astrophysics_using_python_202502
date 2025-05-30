#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 14:19:29 (CST) daisuke>
#

# importing numpy module
import numpy

# sample Numpy array
a = numpy.array ([10.0, 10.1, 9.9, 10.2, 9.8, 10.3, 9.7, \
                  300.0, 10.0, 10.0, 9.9, 9.9, 10.1, 10.1, 10.0])

# making a mask
mask = numpy.array ([False, False, False, False, False, False, False, \
                     True, False, False, False, False, False, False, False])

# making a masked array
a_masked = numpy.ma.array (a, mask=mask)

# printing array "a"
print (f'a:')
print (f'{a}')

# printing mask "mask"
print (f'mask:')
print (f'{mask}')

# printing masked array "a_masked"
print (f'a_masked:')
print (f'{a_masked}')
