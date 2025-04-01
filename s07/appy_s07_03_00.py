#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/01 14:04:43 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# date/time in UT as a string
time_str = '2025-04-15T12:00:00'

# printing "time_str"
print (f'type of "time_str"  = {type (time_str)}')
print (f'value of "time_str" = "{time_str}"')

# constructing Astropy's Time object from a string
time = astropy.time.Time (time_str, format='isot', scale='utc')

# printing "time"
print (f'type of "time"      = {type (time)}')
print (f'value of "time"     = "{time}"')
