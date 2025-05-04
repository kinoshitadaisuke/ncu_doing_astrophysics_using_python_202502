#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:31:32 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'hyg/hyg/v3/hyg_v38.csv.gz'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# making a mask for Vega
obj  = 'Vega'
mask = (table['proper'] == obj)

# printing information of Vega
print (f"object name = {obj}")
print (table[mask]['proper', 'con', 'ra', 'dec', \
                   'mag', 'dist', 'absmag', 'spect'])
