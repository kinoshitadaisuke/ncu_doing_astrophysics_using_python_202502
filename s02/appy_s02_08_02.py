#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:29:31 (CST) daisuke>
#

# importing datetime module
import datetime

# current time in UTC
time_now_utc = datetime.datetime.now (tz=datetime.timezone.utc)

# printing result
print (f'current time in UTC = {time_now_utc}')
