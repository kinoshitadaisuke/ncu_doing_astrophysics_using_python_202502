#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/05 12:25:09 (UT+08:00) daisuke>
#

# importing numpy
import numpy

# output file name
file_output = 'synthetic_02.data'

# parameters
mean      = 100.0
stddev    = 10.0
n_data    = 100000
x_min     = 70.0
x_max     = 130.0
bin_width = 1.0
n_bin     = int ( (x_max - x_min) / bin_width )

# random number generator
rng = numpy.random.default_rng ()

# generation of random numbers
data = rng.normal (loc=mean, scale=stddev, size=n_data)

# making a histogram
stat = numpy.zeros (n_bin)
for rn in data:
    bin_id = int (rn - x_min)
    if ( (bin_id >=0) and (bin_id < n_bin) ):
        stat[bin_id] += 1

# writing data into file
with open (file_output, 'w') as fh_w:
    for i in range (len (stat)):
        x   = i+x_min+bin_width*0.5
        n   = stat[i]/n_data
        err = stat[i]**0.5/n_data
        fh_w.write (f'{x:5.1f} {n:8.6f} {err:8.6f}\n')
