#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/13 09:19:28 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# VOTable file name
file_votable = "m3.vot.gz"

# output file name
file_output = 'm3.list'

# reading VOTable
data_vot = astropy.io.votable.parse_single_table (file_votable)

# printing data type
print (f'data type of "data_vot" = {type (data_vot)}')
