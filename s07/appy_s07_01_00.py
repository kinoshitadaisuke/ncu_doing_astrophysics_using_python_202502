#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:22:19 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# a quantity object of 900.0 sec
t = 900.0 * u_sec

# printing t
print (f't = {t}')
