#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:24:54 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# importing astropy module
import astropy.time

# getting current date/time using datetime module
now_datetime = datetime.datetime.now (tz=datetime.timezone.utc)

# constructing Astropy's Time object from a string
now = astropy.time.Time (now_datetime, scale='utc')

# printing date/time
print (f'now  = {now}')
print (f'     = JD  {now.jd:14.6f}')
print (f'     = MJD {now.mjd:14.6f}')
