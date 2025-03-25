#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/22 22:24:08 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.fits

# input file name
file_input = 'm3.fits'

# opening FITS file
with astropy.io.fits.open (file_input) as hdu_list:
    # printing HDU information
    print (hdu_list.info ())
