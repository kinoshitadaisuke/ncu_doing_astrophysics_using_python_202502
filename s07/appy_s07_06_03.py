#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/22 22:16:48 (UT+8) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# object name
object_name = 'M3'

# survey name
survey = 'DSS2 Red'

# field-of-view
fov_arcmin = 30.0
fov_arcsec = fov_arcmin * 60.0
npixel     = int (fov_arcsec)

# output file name
file_output = 'm3.fits'

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

# getting a list of images
list_image = astroquery.skyview.SkyView.get_image_list (position=coord, \
                                                        survey=survey)

# printing list of images found
print ("images =", list_image)

# getting images
images = astroquery.skyview.SkyView.get_images (position=coord, \
                                                survey=survey, \
                                                pixels=npixel)

# image
image  = images[0]
header = image[0].header
data   = image[0].data

# printing information of image
print (image.info ())

# printing status
print (f'Writing a FITS file "{file_output}"...')

# writing FITS file
hdu = astropy.io.fits.PrimaryHDU (data=data, header=header)
hdu.writeto (file_output)

# printing status
print (f'Done!')
