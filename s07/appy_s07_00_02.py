#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 13:05:14 (UT+8) daisuke>
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
