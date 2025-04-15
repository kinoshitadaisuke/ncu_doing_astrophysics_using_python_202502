#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/05 14:09:05 (UT+8) daisuke>
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
file_data = 'bsc5c.data'

# output files
file_output = 'appy_s09_01_08.png'

# resolution in DPI
resolution_dpi = 150

# lists to store data
list_hr   = []
list_ra   = []
list_dec  = []
list_l    = []
list_b    = []
list_Vmag = []
list_BV   = []

# opening file
with open (file_data, 'r') as fh:
    # counting number of objects
    n = 0
    for line in fh:
        n += 1

# opening file
with open (file_data, 'r') as fh:
    i = 0
    # reading file
    for line in fh:
        # skipping line, if the line starts with '#'
        if (line[0] == '#'):
            continue
        # counting and showing progress
        i += 1
        if (i % 500 == 0):
            print ("progress: %4d / %4d" % (i, n) )
        # splitting line
        (hr_str, ra_str, dec_str, glon_str, glat_str, Vmag_str, BV_str) \
            = line.split ()
        # conversion from string to int or float
        hr = int (hr_str)
        glon_deg = float (glon_str)
        glat_deg = float (glat_str)
        Vmag = float (Vmag_str)
        BV = float (BV_str)

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
        list_BV.append (BV)

# making Numpy arrays
data_hr   = numpy.array (list_hr)
data_ra   = numpy.array (list_ra)
data_dec  = numpy.array (list_dec)
data_l    = numpy.array (list_l)
data_b    = numpy.array (list_b)
data_Vmag = numpy.array (list_Vmag)
data_BV   = numpy.array (list_BV)

# galactic plane
gal_lon   = numpy.linspace (0.001, 359.999, 1000) * u_deg
gal_lat   = numpy.zeros (1000) * u_deg
gal_coord = astropy.coordinates.Galactic (l=gal_lon, \
                                          b=gal_lat)
gal_ra    = gal_coord.transform_to (astropy.coordinates.ICRS ()) \
                     .ra.wrap_at (180.0 * u_deg).radian
gal_dec   = gal_coord.transform_to (astropy.coordinates.ICRS ()).dec.radian

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
ax.plot (gal_ra, gal_dec, \
         linestyle='None', marker='o', color='silver', markersize=5, \
         alpha=0.1, label='Galactic plane')
size   = (8.0 - data_Vmag) * 5.0
colour = 2.0 - data_BV
for j in range ( len (colour) ):
    if (colour[j] < 0.0):
        colour[j] = 0.0
ax.scatter (data_ra, data_dec, \
            marker='o', s=size, \
            c=colour, cmap=matplotlib.cm.Spectral, alpha=0.25)

# saving figure to files
fig.savefig (file_output, dpi=resolution_dpi, bbox_inches="tight")
