#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:15:34 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'finding kurtosis of distribution'
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

# calculation of arithmetic mean of distribution
mean = scipy.stats.tmean (rg)

# calculation of variance of distribution
var = scipy.stats.tvar (rg)

# calculation of standard deviation of distribution
stddev  = scipy.stats.tstd (rg)
pstddev = scipy.stats.tstd (rg, ddof=0)

# calculation of zeroth moment about the mean
moment_0 = scipy.stats.moment (rg, moment=0)

# calculation of first moment about the mean
moment_1 = scipy.stats.moment (rg, moment=1)

# calculation of second moment about the mean
moment_2 = scipy.stats.moment (rg, moment=2)

# calculation of third moment about the mean
moment_3 = scipy.stats.moment (rg, moment=3)

# calculation of fourth moment about the mean
moment_4 = scipy.stats.moment (rg, moment=4)

# calculation of skewness
skew = scipy.stats.skew (rg)

# calculation of skewness using third moment and standard deviation
skew2 = moment_3 / pstddev**3

# calculation of kurtosis
kurtosis = scipy.stats.kurtosis (rg, fisher=False)

# calculation of kurtosis of Fisher's definition
kurtosis_ex = scipy.stats.kurtosis (rg)

# printing minimum and maximum values
print (f'statistical values:')
print (f'  tmin          = {tmin:15.6f}')
print (f'  tmax          = {tmax:15.6f}')
print (f'  mean          = {mean:15.6f}')
print (f'  var           = {var:15.6f}')
print (f'  sample stddev = {stddev:15.6f}')
print (f'  pop. stddev   = {pstddev:15.6f}')
print (f'  zeroth moment = {moment_0:15.6f}')
print (f'  first moment  = {moment_1:15.6f}')
print (f'  second moment = {moment_2:15.6f}')
print (f'  third moment  = {moment_3:15.6f}')
print (f'  fourth moment = {moment_4:15.6f}')
print (f'  skewness      = {skew:15.6f}')
print (f'  skewness2     = {skew2:15.6f}')
print (f'  kurtosis      = {kurtosis:15.6f}')
print (f'  kurtosis_ex   = {kurtosis_ex:15.6f}')
