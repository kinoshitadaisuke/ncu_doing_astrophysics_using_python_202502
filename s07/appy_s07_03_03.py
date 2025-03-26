#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:24:58 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# getting current date/time
now = astropy.time.Time.now ()

# printing date/time
print (f'now  = {now}')
print (f'     = JD  {now.jd:14.6f}')
print (f'     = MJD {now.mjd:14.6f}')
