#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/10 08:42:26 (CST) daisuke>
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
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# importing gzip module
import gzip

# constructing a parser object
descr  = f'Positions of Sun, Moon, planets, and bright stars on Az-El plot'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-b', '--bsc5', default='bsc5.gz', \
                     help='compressed data file of BSC5 (default: bsc5.gz)')
parser.add_argument ('-m', '--maglimit', type=float, default=3.5, \
                     help='magnitude limit (default: 3.5)')
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('-t', '--time', default='2000-01-01T12:00:00', \
                     help='start date/time in YYYY-MM-DDThh:mm:ss format')
parser.add_argument ('-l', '--longitude', type=float, default=121.186667, \
                     help='longitude in deg (default: 121.186667)')
parser.add_argument ('-p', '--latitude', type=float, default=24.970000, \
                     help='latitude in deg (default: 24.970000)')
parser.add_argument ('-e', '--height', type=float, default=151.6, \
                     help='elevation in metre (default: 151.6)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_bsc5      = args.bsc5
mag_limit      = args.maglimit
file_output    = args.output
resolution_dpi = args.resolution
datetime_start = args.time
longitude_deg  = args.longitude
latitude_deg   = args.latitude
height_m       = args.height

# unit
u_deg = astropy.units.deg
u_m   = astropy.units.m

# time
t_start = astropy.time.Time (datetime_start, format='isot', scale='utc')

# location of observer
longitude = longitude_deg * u_deg
latitude  = latitude_deg * u_deg
height    = height_m * u_m

# if "file_output" is empty, then stop the script
if (file_output == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: need to specify output file name!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# making pathlib object
path_bsc5   = pathlib.Path (file_bsc5)
path_output = pathlib.Path (file_output)

# existence check of BSC5 catalogue file
if not (path_bsc5.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: catalogue file "{file_bsc5}" does not exist!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

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
    
# making an empty list for storing star data
list_star = []

# printing status
print (f'Now, reading Bright Star Catalogue...')

# opening BSC catalogue file
with gzip.open (file_bsc5, 'rb') as fh:
    # reading BSC catalogue line-by-line
    for line in fh:
        # hour of RA
        ra_h_str = line[75:77].strip ()
        # minute of RA
        ra_m_str = line[77:79].strip ()
        # second of RA
        ra_s_str = line[79:83].strip ()
        # sign of Dec
        dec_sign = line[83:84].decode ('utf-8')
        # degree of Dec
        dec_d_str = line[84:86].strip ()
        # arcmin of Dec
        dec_m_str = line[86:88].strip ()
        # arc sec of Dec
        dec_s_str = line[88:90].strip ()
        # V-band magnitude
        mag_V_str = line[102:107].strip ()

        # if coordinate is missing, then skip
        if (ra_h_str == ''):
            continue

        # conversion from string to int and float
        try:
            ra_h  = int (ra_h_str)
            ra_m  = int (ra_m_str)
            ra_s  = float (ra_s_str)
            dec_d = int (dec_d_str)
            dec_m = int (dec_m_str)
            dec_s = float (dec_s_str)
            mag_V = float (mag_V_str)
        except:
            continue

        # if magnitude is fainter than mag_limit, then skip
        if (mag_V > mag_limit):
            continue

        # RA in deg
        ra_deg = (ra_h + ra_m / 60.0 + ra_s / 3600.0) * 15.0
        if (dec_sign == '-'):
            dec_deg = (dec_d + dec_m / 60.0 + dec_s / 3600.0) * -1.0
        else:
            dec_deg = dec_d + dec_m / 60.0 + dec_s / 3600.0

        # appending data to the list
        list_star.append ( [ra_deg, dec_deg, mag_V] )

# printing status
print (f'Finished reading Bright Star Catalogue!')

# printing status
print (f'Now, generating a plot...')

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

# processing each solar system body
for name in dict_solsys.keys ():
    # setting a query
    query = astroquery.jplhorizons.Horizons (id_type=None,
                                             id=dict_solsys[name]['id'], \
                                             location={
                                                 'lon': longitude,
                                                 'lat': latitude,
                                                 'elevation': height,
                                                 }, \
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

# processing each star
for i in range (len (list_star)):
    # RA, Dec, and V-band magnitude
    ra_deg  = list_star[i][0]
    dec_deg = list_star[i][1]
    mag_V   = list_star[i][2]
    # making a SkyCoord object of Astropy
    coord = astropy.coordinates.SkyCoord (ra_deg, dec_deg, unit=(u_deg, u_deg))
    # making an observer object
    observer = astropy.coordinates.EarthLocation (longitude, latitude, height)
    # conversion from (RA, Dec) into (Az, El)
    altaz     = astropy.coordinates.AltAz (obstime=t_start, location=observer)
    obj_altaz = coord.transform_to (altaz)
    obj_alt   = obj_altaz.alt.deg
    obj_az    = obj_altaz.az.deg
    # plotting data
    if (obj_alt > 0.0):
        # r and theta
        obj_r     = 90.0 - obj_alt
        obj_theta = numpy.deg2rad (obj_az)
        # plotting data point
        if (list_star[i][2] < 0.5):
            ax.plot (obj_theta, obj_r, \
                     linestyle='None', marker='o', \
                     markersize=5, \
                     color='deepskyblue')
        elif ( (list_star[i][2] >= 0.5) and (list_star[i][2] < 1.5) ):
            ax.plot (obj_theta, obj_r, \
                     linestyle='None', marker='o', \
                     markersize=4, \
                     color='deepskyblue')
        elif ( (list_star[i][2] >= 1.5) and (list_star[i][2] < 2.5) ):
            ax.plot (obj_theta, obj_r, \
                     linestyle='None', marker='o', \
                     markersize=3, \
                     color='deepskyblue')
        elif ( (list_star[i][2] >= 2.5) and (list_star[i][2] < 3.5) ):
            ax.plot (obj_theta, obj_r, \
                     linestyle='None', marker='o', \
                     markersize=2, \
                     color='deepskyblue')
        elif ( (list_star[i][2] >= 3.5) and (list_star[i][2] < 4.5) ):
            ax.plot (obj_theta, obj_r, \
                     linestyle='None', marker='o', \
                     markersize=1, \
                     color='deepskyblue')
        else:
            ax.plot (obj_theta, obj_r, \
                     linestyle='None', marker='o', \
                     markersize=0.5, \
                     color='deepskyblue')
        
# title
ax.set_title (f'Sky on {t_start.iso} at ({longitude:7.3f}, {latitude:7.3f})')
  
# legend
a = 0.0
legend_x = 0.5 * numpy.cos (a) + 0.50
legend_y = 0.5 * numpy.sin (a) + 0.45
ax.legend (loc='upper left', bbox_to_anchor=(legend_x, legend_y))

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)

# printing status
print (f'Finished generating a plot!')
