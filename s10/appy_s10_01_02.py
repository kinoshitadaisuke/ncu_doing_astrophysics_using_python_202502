#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:18:53 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'honey-badger/examples/planets/planets.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing column names of astropy table
print (table.info ())
