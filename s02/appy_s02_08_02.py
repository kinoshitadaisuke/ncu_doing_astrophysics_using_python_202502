#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 17:16:04 (UT+8) daisuke>
#

# importing datetime module
import datetime

# current time in UTC
time_now_utc = datetime.datetime.now (tz=datetime.timezone.utc)

# printing result
print (f'current time in UTC = {time_now_utc}')
