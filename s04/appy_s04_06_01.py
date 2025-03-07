#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/07 15:53:06 (CST) daisuke>
#

# input data file
file_input = 'alf_ori.data'

# opening input file
with open (file_input, 'r') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # splitting data
        (date, mag_str, error_str, band, telescope) = line.split ()
        # conversion from string to float
        mag       = float (mag_str)
        mag_error = float (error_str)
        # printing data
        print (f'{date} {mag:f} {mag_error:f} {band} {telescope}')
