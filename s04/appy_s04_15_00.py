#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/11 13:28:09 (CST) daisuke>
#

# importing astropy module
import astropy.io.fits

# input FITS file name
file_fits = 'hltau_alma.fits'

# opening FITS file
with astropy.io.fits.open (file_fits) as hdu_list:
    # printing basic information of FITS file
    print (hdu_list.info ())
