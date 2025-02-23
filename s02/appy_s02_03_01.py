#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 16:10:24 (UT+8) daisuke>
#

# input file name
file_input = 'pi_1000.txt'

# opening file for reading
with open (file_input, 'r') as fh_read:
    # reading file line-by-line
    for line in fh_read:
        # printing line
        print (f'{line}', end='')
