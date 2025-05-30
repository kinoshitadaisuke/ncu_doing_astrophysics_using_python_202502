#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:12:25 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'generating a set of random numbers of uniform distribution'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-n', '--number', type=int, default=1, \
                     help='number of random numbers (default: 1)')
parser.add_argument ('-a', '--min', type=float, default=0.0, \
                     help='minimum value of random numbers (default: 0.0)')
parser.add_argument ('-b', '--max', type=float, default=1.0, \
                     help='maximum value of random numbers (default: 1.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
n     = args.number
v_min = args.min
v_max = args.max

# range
v_range = v_max - v_min

# generating a set of random numbers of uniform distribution
ru = scipy.stats.uniform.rvs (loc=v_min, scale=v_range, size=n)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{ru}')
