#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/22 22:09:28 (UT+8) daisuke>
#

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad

# object name
object_name = 'Antares'

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
