#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:29:00 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'hyg/hyg/v3/hyg_v38.csv.gz'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing astropy table
print (table)
