#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:27:11 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits

# input file name
file_input = 'm3.fits'

# opening FITS file
with astropy.io.fits.open (file_input) as hdu_list:
    # printing HDU information
    print (hdu_list.info ())
