#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:21:35 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants

# speeed of light in vacuum
c = astropy.constants.c

# calculation
v = 0.01 * c

# object type of "c"
type_c = type (c)

# object type of "v"
type_v = type (v)

# printing object type of "c"
print (f'type of "c" = {type_c}')

# printing object type of "v"
print (f'type of "v" = {type_v}')
