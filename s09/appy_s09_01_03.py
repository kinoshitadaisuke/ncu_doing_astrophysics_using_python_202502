#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/05 11:49:42 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.units
import astropy.coordinates

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# data file
file_data = 'bsc5.data'

# output files
file_output = 'appy_s09_01_03.png'

# resolution in DPI
resolution_dpi = 150

# lists to store data
list_hr   = []
list_ra   = []
list_dec  = []
list_l    = []
list_b    = []
list_Vmag = []

# opening file
with open (file_data, 'r') as fh:
    # counting number of objects
    n = 0
    for line in fh:
        n += 1

# opening file
with open (file_data, 'r') as fh:
    # initialising counter
    i = 0
    # reading file
    for line in fh:
        # counting and showing progress
        i += 1
        if (i % 500 == 0):
            print ("progress: %4d / %4d" % (i, n) )
        # splitting line
        (hr_str, ra_str, dec_str, glon_str, glat_str, Vmag_str) = line.split ()
        # conversion from string to int or float
        hr       = int (hr_str)
        glon_deg = float (glon_str)
        glat_deg = float (glat_str)
        Vmag     = float (Vmag_str)

        # skip if Vmag > 6.0
        if (Vmag > 6.0):
            continue
    
        # coordinate
        coord = astropy.coordinates.SkyCoord (ra_str, dec_str, \
                                              frame=astropy.coordinates.FK5, \
                                              equinox="J2000", \
                                              unit=(u_ha, u_deg) )

        # (RA, Dec) in radian
        ra_rad = coord.ra.radian
        dec_rad = coord.dec.radian
        # conversion from (RA, Dec) to (l, b) using astropy
        l_rad = coord.galactic.l.radian
        b_rad = coord.galactic.b.radian

        # changing from [0:2pi] to [-pi:pi]
        if (ra_rad > numpy.pi):
            ra_rad -= 2.0 * numpy.pi
        if (l_rad > numpy.pi):
            l_rad -= 2.0 * numpy.pi

        # appending data to lists
        list_hr.append (hr)
        list_ra.append (ra_rad)
        list_dec.append (dec_rad)
        list_l.append (l_rad)
        list_b.append (b_rad)
        list_Vmag.append (Vmag)

# making Numpy arrays
data_hr   = numpy.array (list_hr)
data_ra   = numpy.array (list_ra)
data_dec  = numpy.array (list_dec)
data_l    = numpy.array (list_l)
data_b    = numpy.array (list_b)
data_Vmag = numpy.array (list_Vmag)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection="hammer")

# axes
ax.grid ()
ax.set_title ('Bright Star Catalogue', loc='right')
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting data
size = (6.5 - data_Vmag) * 5.0
ax.scatter (data_ra, data_dec, marker='o', s=size, c='blue', alpha=0.3)

# saving figure to files
fig.savefig (file_output, dpi=resolution_dpi, bbox_inches="tight")
