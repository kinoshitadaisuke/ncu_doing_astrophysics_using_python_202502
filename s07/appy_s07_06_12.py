#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/03 13:07:27 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.units
import astropy.coordinates
import astropy.wcs

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# object name
object_name = 'Horsehead Nebula'

# survey name
survey = 'DSS2 Red'

# field-of-view
fov_arcmin = 20.0
fov_arcsec = fov_arcmin * 60.0
npixel     = int (fov_arcsec)

# FITS file name
file_fits = 'horsehead.fits'

# PNG file name
file_png = 'horsehead.png'

# colour map
cmap = 'magma'

# resolution in DPI
resolution_dpi = 225

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# name resolver
query_result = astroquery.simbad.Simbad.query_object (object_name)

# coordinate from Simbad
ra_deg  = query_result['ra'][0]
dec_deg = query_result['dec'][0]

# making SkyCoord object of astropy
coord = astropy.coordinates.SkyCoord (ra_deg, dec_deg, frame='icrs', unit=u_deg)

# RA and Dec of coordinate in sexagesimal format
(ra, dec) = coord.to_string (style='hmsdms').split ()

# printing result
print (f'Target name: "{object_name}"')
print (f'  RA  = {ra:20s} = {coord.ra.deg:10.6f} [deg]')
print (f'  Dec = {dec:20s} = {coord.dec.deg:+10.6f} [deg]')

# clearing astroquery skyview cache
astroquery.skyview.SkyView.clear_cache ()

# getting a list of images
list_image = astroquery.skyview.SkyView.get_image_list (position=coord, \
                                                        survey=survey)

# printing a list of images found
print ("images =", list_image)

# getting images
images = astroquery.skyview.SkyView.get_images (position=coord, \
                                                survey=survey, \
                                                pixels=npixel)

# image
image  = images[0]
header = image[0].header
data   = image[0].data

# printing image information
print (image.info ())

# printing status
print (f'Writing a FITS file "{file_fits}"...')

# writing FITS file
hdu = astropy.io.fits.PrimaryHDU (data=data, header=header)
hdu.writeto (file_fits, overwrite=True)

# printing status
print (f'Done!')

# opening FITS file
with astropy.io.fits.open (file_fits) as hdu_list:
    # printing HDU information
    print (hdu_list.info ())
    
    # reading FITS header, WCS information, and image data
    header = hdu_list[0].header
    wcs    = astropy.wcs.WCS (header)
    image  = hdu_list[0].data

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection=wcs)

# axes
ax.set_title (object_name)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# normalisation
norm \
    = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.AsinhStretch () )

# plotting image
im = ax.imshow (image, origin='lower', cmap=cmap, norm=norm)
fig.colorbar (im)

# printing status
print (f'{file_fits} ==> {file_png}')

# saving file
fig.savefig (file_png, dpi=resolution_dpi)
