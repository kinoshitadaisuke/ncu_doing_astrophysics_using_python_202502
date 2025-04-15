#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/04 14:16:58 (UT+8) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# date/time
date = astropy.time.Time ('2025-01-01 00:00:00')

# target asteroid name
asteroid = 'Ceres'

# set-up a query for JPL Horizons
query = astroquery.jplhorizons.Horizons (id=asteroid, \
                                         id_type='smallbody', \
                                         epochs=date.jd)

# fetching ephemeris of asteroid
eph = query.ephemerides ()

# printing position of asteroid
print (f"Ephemeris of asteroid '{eph['targetname'][0]}' at {date}:")
print (f"  RA  = {eph['RA'][0]:8.4f} deg")
print (f"  Dec = {eph['DEC'][0]:+8.4f} deg")
