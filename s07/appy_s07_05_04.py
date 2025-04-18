#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:26:39 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.stats

# parameters for random number generation
mean   = 1000.0
stddev = 30.0
n      = 10**4

# generation of a set of random number of Gaussian distribution
rng  = numpy.random.default_rng ()
data = rng.normal (loc=mean, scale=stddev, size=n)

# printing generated data
print (f'Genearated random numbers:')
print (f'{data}')
print (f'Number of random numbers generated: {len (data)}')

# mean and stddev
mean0   = numpy.mean (data)
median0 = numpy.median (data)
stddev0 = numpy.std (data)

# printing results
print (f'Simple mean and stddev before adding outliers:')
print (f'  mean0   = {mean0}')
print (f'  median0 = {median0}')
print (f'  stddev0 = {stddev0}')

# printing status
print (f'Now, adding some outliers to the dataset...')

# adding some outliers
data[0]    +=  2000.0
data[1000] +=  3000.0
data[2000] +=  4000.0
data[3000] +=  5000.0
data[4000] +=  6000.0
data[5000] +=  7000.0
data[6000] +=  8000.0
data[7000] +=  9000.0
data[8000] += 10000.0
data[9000] += 11000.0

# printing status
print (f'Finished adding some outliers to the dataset!')

# printing data with some outliers
print (f'After adding some outliers:')
print (f'{data}')
print (f'Number of random numbers generated: {len (data)}')

# mean and stddev
mean1   = numpy.mean (data)
median1 = numpy.median (data)
stddev1 = numpy.std (data)

# printing results
print (f'Simple mean and stddev after adding outliers:')
print (f'  mean1   = {mean1}')
print (f'  median1 = {median1}')
print (f'  stddev1 = {stddev1}')

# sigma clipping
mean2, median2, stddev2 = astropy.stats.sigma_clipped_stats (data, \
                                                             sigma=3.0, \
                                                             maxiters=10)

# sigma-clipped mean and staddev
print (f'Sigma-clipped mean and stddev:')
print (f'  mean2   = {mean2}')
print (f'  median2 = {median2}')
print (f'  stddev2 = {stddev2}')
