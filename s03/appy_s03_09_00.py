#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 14:07:50 (CST) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.default_rng ()

# generating a random number of uniform distribution between 0 and 1
array_x = rng.random ()

# printing generated random numbers
print (f'{array_x}')
