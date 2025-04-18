#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:13:57 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'finding minimum and maximum values'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-n', '--number', type=int, default=1, \
                     help='number of random numbers (default: 1)')
parser.add_argument ('-m', '--mean', type=float, default=0.0, \
                     help='mean value of distribution (default: 0.0)')
parser.add_argument ('-s', '--stddev', type=float, default=1.0, \
                     help='standard deviation of distribution (default: 1.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
n_rg      = args.number
mean_rg   = args.mean
stddev_rg = args.stddev

# generating a set of random numbers of Gaussian distribution
rg = scipy.stats.norm.rvs (loc=mean_rg, scale=stddev_rg, size=n_rg)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{rg}')

# finding minimum value
tmin = scipy.stats.tmin (rg)

# finding maximum value
tmax = scipy.stats.tmax (rg)

# printing minimum and maximum values
print (f'statistical values:')
print (f'  tmin = {tmin:15.6f}')
print (f'  tmax = {tmax:15.6f}')
