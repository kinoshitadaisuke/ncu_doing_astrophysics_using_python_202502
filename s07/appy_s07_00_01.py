#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 12:58:42 (UT+8) daisuke>
#

# importing astropy module
import astropy.constants

# speeed of light in vacuum
c = astropy.constants.c

# calculation
v = 0.01 * c

# printing c and v
print (f'c = {c}')
print (f'v = 0.01 * {c}')
print (f'  = {v}')
