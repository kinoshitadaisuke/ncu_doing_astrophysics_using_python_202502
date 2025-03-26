#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:21:29 (UT+08:00) daisuke>
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
