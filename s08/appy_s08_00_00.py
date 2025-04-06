#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/06 14:55:38 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

#
# constants
#

# speed of light in vacuum
c = scipy.constants.physical_constants['speed of light in vacuum']

# Planck constant
h = scipy.constants.physical_constants['Planck constant']

# Boltzmann constant
k = scipy.constants.physical_constants['Boltzmann constant']

# printing values and units of constants
print (f'Constants:')
print (f'  c = {c[0]:g} [{c[1]}]')
print (f'  h = {h[0]:g} [{h[1]}]')
print (f'  k = {k[0]:g} [{k[1]}]')
