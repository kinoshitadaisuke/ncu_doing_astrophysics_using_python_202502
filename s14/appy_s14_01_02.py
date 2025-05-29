#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/29 10:54:00 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# target name
target = 'Sun'

# observatory (D35 ==> Lulin Observatory)
#
# To get a list of available observatory codes, visit following web page.
#   https://www.minorplanetcenter.net/iau/lists/ObsCodes.html
#
obs_site = 'D35'

# date/time
t  = astropy.time.Time ('2025-07-01T04:00:00', scale='utc', format='isot')
jd = t.jd

# sending a query to NASA/JPL Horizons system
obj = astroquery.jplhorizons.Horizons (id_type=None, id=target, \
                                       location=obs_site, epochs=jd)

# getting ephemerides
ephemerides = obj.ephemerides ()

# printing ephemerides
print (ephemerides.info)
