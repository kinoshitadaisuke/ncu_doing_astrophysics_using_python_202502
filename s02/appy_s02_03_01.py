#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:20:59 (CST) daisuke>
#

# input file name
file_input = 'pi_1000.txt'

# opening file for reading
with open (file_input, 'r') as fh_read:
    # reading file line-by-line
    for line in fh_read:
        # printing line
        print (f'{line}', end='')
