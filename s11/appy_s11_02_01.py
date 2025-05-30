#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/13 09:05:54 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'm1.fits'

# output file name
file_output = 'm1.png'

# resolution in DPI
resolution_dpi = 150.0

# colour map
colour_map = 'bone'

# reading FITS file
with astropy.io.fits.open (file_input) as hdu:
    # reading header
    header = hdu[0].header
    # WCS information
    wcs = astropy.wcs.WCS (header)
    # reading image
    image  = hdu[0].data

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection=wcs)

# axes
ax.set_title (file_input)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting image
norm = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.AsinhStretch () )
im = ax.imshow (image, origin='lower', cmap=colour_map, norm=norm)
fig.colorbar (im)

# saving file
fig.savefig (file_output, dpi=resolution_dpi)
