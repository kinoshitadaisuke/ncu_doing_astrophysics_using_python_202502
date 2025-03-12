#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/06 20:02:49 (UT+8) daisuke>
#

# importing scipy module
import scipy.constants

# some units for length
angstrom = scipy.constants.angstrom
au       = scipy.constants.au
ly       = scipy.constants.light_year
parsec   = scipy.constants.parsec

# printing units for length
print (f'1 angstrom = {angstrom:g} [m]')
print (f'1 au       = {au:g} [m]')
print (f'1 ly       = {ly:g} [m]')
print (f'1 parsec   = {parsec:g} [m]')
