#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/10 08:40:29 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# constructing a parser object
descr  = f'Position of the Moon on Az-El plot'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-c', '--obscode', default='D35', \
                     help='observatory code (default: D35)')
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('-t', '--time', default='2000-01-01T12:00:00', \
                     help='start date/time in YYYY-MM-DDThh:mm:ss format')

# parsing arguments
args = parser.parse_args ()

# parameters
obscode        = args.obscode
file_output    = args.output
resolution_dpi = args.resolution
datetime_start = args.time

# if "file_output" is empty, then stop the script
if (file_output == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: need to specify output file name!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# making pathlib object
path_output = pathlib.Path (file_output)

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: output file "{file_output}" already exists!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# time
t_start = astropy.time.Time (datetime_start, format='isot', scale='utc')

# setting a query
query_moon = astroquery.jplhorizons.Horizons (id_type=None, id='301', \
                                              location=f'{obscode}', \
                                              epochs=t_start.jd)

# getting the position of the Moon
eph_moon = query_moon.ephemerides ()

# azimuth and elevation of the Moon
moon_az_deg = eph_moon["AZ"][0]
moon_el_deg = eph_moon["EL"][0]

# printing the position of the Moon
print (f'Date/Time: {t_start.iso}')
print (f'  Moon:')
print (f'    AZ = {moon_az_deg} [deg]')
print (f'    EL = {moon_el_deg} [deg]')

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='polar')

# coordinate settings
ax.set_rlim (0.0, 90.0)
ax.grid (True)
ax.set_rgrids ( numpy.linspace (0.0, 90.0, 10),
                labels=('') * 10,
                fontsize=12)
ax.set_thetagrids ( numpy.linspace (0.0, 315.0, 8),
                    labels=('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'),
                    fontsize=16)
ax.set_theta_zero_location ('N')

# r and theta
moon_r     = 90.0 - moon_el_deg
moon_theta = numpy.deg2rad (moon_az_deg)

# plotting data
ax.plot (moon_theta, moon_r, \
         linestyle='None', marker='o', markersize=15, color='yellow', \
         label='Moon')

# title
ax.set_title (f'Sky on {t_start.iso} at {obscode}')

# legend
a = 0.0
legend_x = 0.5 * numpy.cos (a) + 0.50
legend_y = 0.5 * numpy.sin (a) + 0.45
ax.legend (loc='upper left', bbox_to_anchor=(legend_x, legend_y))

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)
