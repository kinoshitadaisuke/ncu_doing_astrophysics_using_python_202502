#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/02 14:13:54 (CST) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10^6 random numbers of uniform distribution 
# between 1000 and 2000
array_x = rng.uniform (1000.0, 2000.0, 10**6)

# printing generated random numbers
print (f'{array_x}')

# printing number of data
print (f'number of data = {len (array_x):g}')

# statistical values calculated by numpy module
mean_n     = numpy.mean (array_x)
median_n   = numpy.median (array_x)
variance_n = numpy.var (array_x)
stddev_n   = numpy.std (array_x)

# printing statistical values
print (f'statistical values by Numpy:')
print (f'  mean     = {mean_n:10.3f}')
print (f'  median   = {median_n:10.3f}')
print (f'  variance = {variance_n:10.3f}')
print (f'  stddev   = {stddev_n:10.3f}')

# statistical values calculated by statistics module
mean_s     = statistics.fmean (array_x)
median_s   = statistics.median (array_x)
variance_s = statistics.pvariance (array_x)
stddev_s   = statistics.pstdev (array_x)

# printing statistical values
print (f'statistical values by statistics module:')
print (f'  mean     = {mean_s:10.3f}')
print (f'  median   = {median_s:10.3f}')
print (f'  variance = {variance_s:10.3f}')
print (f'  stddev   = {stddev_s:10.3f}')
