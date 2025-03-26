#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:25:08 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# time t1
t1 = astropy.time.Time ('2024-01-01 00:00:00', format='iso', scale='utc')

# time t2
t2 = astropy.time.Time ('2025-01-01 00:00:00', format='iso', scale='utc')

# time between t1 and t2
delta_t = t2 - t1

# printing date/time
print (f't1      = {t1}')
print (f't2      = {t2}')
print (f't2 - t1 = {delta_t} day = {delta_t.sec:g} sec')
