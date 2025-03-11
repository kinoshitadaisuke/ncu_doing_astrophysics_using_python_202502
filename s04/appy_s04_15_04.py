#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/11 23:00:04 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# input FITS file name
file_fits = 'hltau_alma.fits'

# output PNG file name
file_output = 'appy_s04_15_04.png'

# opening FITS file
with astropy.io.fits.open (file_fits) as hdu_list:
    # printing basic information of FITS file
    print (hdu_list.info ())
    # reading FITS header, WCS information, and image data
    image  = hdu_list[0].data[0][0]
    # printing image data
    print (f'shape of image data')
    print (f'  ndim  = {image.ndim}')
    print (f'  shape = {image.shape}')
    print (f'image data:')
    print (image)

# cropping image
image_cropped = image[350:430,360:440]

# printing cropped image
print (f'shape of image_cropped')
print (f'  ndim  = {image_cropped.ndim}')
print (f'  shape = {image_cropped.shape}')
print (f'image_cropped:')
print (image_cropped)
   
# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a contour map
contour = ax.contour (image_cropped, levels=numpy.linspace (0.0, 0.15, 6))
ax.clabel (contour)

# axes
ax.set_xlabel ('X')
ax.set_ylabel ('Y')
ax.set_title ('HL Tau observed by ALMA')

# saving a plot as a file
fig.savefig (file_output, dpi=150)
