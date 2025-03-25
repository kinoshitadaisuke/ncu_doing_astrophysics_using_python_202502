#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/22 22:34:41 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.wcs

# input file name
file_input = 'm3.fits'

# opening FITS file
with astropy.io.fits.open (file_input) as hdu_list:
    # printing HDU information
    print (hdu_list.info ())

    # reading FITS header, WCS information, and image data
    header = hdu_list[0].header
    wcs    = astropy.wcs.WCS (header)
    image  = hdu_list[0].data

# printing data types of the header, wcs, and image
print (f'type of "header" : {type (header)}')
print (f'type of "wcs"    : {type (wcs)}')
print (f'type of "image"  : {type (image)}')

# printing image data
print ()
print (f'ndim of image data  : {image.ndim}')
print (f'shape of image data : {image.shape}')
print (f'size of image data  : {image.size}')
print ()
print (f'image data of FITS file "{file_input}":')
print (image)
