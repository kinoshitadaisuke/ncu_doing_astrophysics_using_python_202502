#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/10 08:41:24 (CST) daisuke>
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
descr  = f'Positions of Sun, Moon, and planets on Az-El plot'
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

# list of major bodies in solar system
#  Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn
dict_solsys = {
    'Sun': {
        'id': '10',
        'size': 15,
        'colour': 'orange',
        },
    'Moon': {
        'id': '301',
        'size': 12,
        'colour': 'yellow',
        },
    'Mercury': {
        'id': '199',
        'size': 6,
        'colour': 'indigo',
        },
    'Venus': {
        'id': '299',
        'size': 10,
        'colour': 'lime',
        },
    'Mars': {
        'id': '499',
        'size': 8,
        'colour': 'red',
        },
    'Jupiter': {
        'id': '599',
        'size': 10,
        'colour': 'tan',
        },
    'Saturn': {
        'id': '699',
        'size': 10,
        'colour': 'bisque',
        },
    'Uranus': {
        'id': '799',
        'size': 6,
        'colour': 'aqua',
        },
    'Neptune': {
        'id': '899',
        'size': 6,
        'colour': 'royalblue',
        },
}
    
# time
t_start = astropy.time.Time (datetime_start, format='isot', scale='utc')

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

# processing each body
for name in dict_solsys.keys ():
    # setting a query
    query = astroquery.jplhorizons.Horizons (id_type=None,
                                             id=dict_solsys[name]['id'], \
                                             location=f'{obscode}', \
                                             epochs=t_start.jd)

    # getting the position
    eph = query.ephemerides ()

    # azimuth and elevation
    az_deg = eph["AZ"][0]
    el_deg = eph["EL"][0]

    # printing the position
    if (name == 'Sun'):
        print (f'Date/Time: {t_start.iso}')
    print (f'  {name}:')
    print (f'    AZ = {az_deg:6.2f} [deg]')
    print (f'    EL = {el_deg:6.2f} [deg]')

    # plotting data
    if (el_deg > 0.0):
        # r and theta
        obj_r     = 90.0 - el_deg
        obj_theta = numpy.deg2rad (az_deg)
        # plotting data point
        ax.plot (obj_theta, obj_r, \
                 linestyle='None', marker='o', \
                 markersize=dict_solsys[name]['size'], \
                 color=dict_solsys[name]['colour'], \
                 label=name)

# title
ax.set_title (f'Sky on {t_start.iso} at {obscode}')
  
# legend
a = 0.0
legend_x = 0.5 * numpy.cos (a) + 0.50
legend_y = 0.5 * numpy.sin (a) + 0.45
ax.legend (loc='upper left', bbox_to_anchor=(legend_x, legend_y))

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)
