#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/21 15:33:22 (UT+8) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# units
u_m = astropy.units.m

# date/time in UTC
t_str = '2035-09-02 01:56:46.3'
t_utc = astropy.time.Time (t_str, format='iso', scale='utc')

# location of observer: Mito, Japan
longitude = '140d28m16.5s'
latitude  = '+36d21m57s'
height    = 0.0 * u_m
observer  = astropy.coordinates.EarthLocation (longitude, latitude, height)

# getting position of the Sun
sun = astropy.coordinates.get_body ('sun', t_utc, location=observer)

# getting position of the Moon
moon = astropy.coordinates.get_body ('moon', t_utc, location=observer)

# RA and Dec
(sun_ra, sun_dec)   = sun.to_string ('hmsdms').split ()
(moon_ra, moon_dec) = moon.to_string ('hmsdms').split ()

# calculation of angular distance
separation = sun.separation (moon)

# printing result of calculation
print (f'Position of the Sun:')
print (f'  (RA, Dec) = ({sun_ra}, {sun_dec})')
print (f'Position of the Moon:')
print (f'  (RA, Dec) = ({moon_ra}, {moon_dec})')
print (f'Angular distance between the Sun and the Moon on {t_utc}')
print (f'  separation = {separation}')
