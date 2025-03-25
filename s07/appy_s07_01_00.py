#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 13:30:16 (UT+8) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# a quantity object of 900.0 sec
t = 900.0 * u_sec

# printing t
print (f't = {t}')
