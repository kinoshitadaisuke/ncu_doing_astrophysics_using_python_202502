#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 12:05:14 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# file
file_data = 'ned1d_new.csv'

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# printing astropy table summary information
print (rawdata.info ())
