#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/06 15:03:12 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'appy_s08_00_14.png'

# resolution in DPI
resolution_dpi = 150

#
# function to calculate blackbody curve
#
def bb_lambda (wavelength, T):
    # speed of light in vacuum
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Planck constant
    h = scipy.constants.physical_constants['Planck constant']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Planck function
    blackbody = 2.0 * h[0] * c[0]**2 / wavelength**5 \
        / (numpy.exp (h[0] * c[0] / (wavelength * k[0] * T) ) - 1.0 )

    # returning blackbody radiation curve
    return (blackbody)

# temperature of blackbody
T = 2000.0

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T} K')

# range of wavelength (from 10**-7 m = 100 nm to 10**-3 m = 1 mm)
wavelength_min = -7.0
wavelength_max = -3.0

# wavelength in metre
wavelength = numpy.logspace (wavelength_min, wavelength_max, num=5001)

# T = 2000 K blackbody spectrum
bb_2000 = bb_lambda (wavelength, T)

# printing Planck function
print (f'Wavelength:')
print (f'{wavelength}')
print (f'Planck function:')
print (f'{bb_2000}')

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel (r'Wavelength [$\mu$m]')
ax.set_ylabel (r'Specific Intensity [W sr$^{-1}$ m$^{-3}$]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (0.03, 1000.0)
ax.set_ylim (10**0, bb_2000.max () * 3)

# showing UV region
ax.fill_between ([0.03, 0.3], 10**-2, 10**18, color='violet', alpha=0.1)
ax.text (x=0.1, y=10**1, s='UV')

# showing visible region
ax.fill_between ([0.3, 1.0], 10**-2, 10**18, color='green', alpha=0.1)
ax.text (x=0.35, y=10**1, s='Visible')

# showing IR region
ax.fill_between ([1.0, 1000.0], 10**-2, 10**18, color='red', alpha=0.1)
ax.text (x=3.0, y=10**1, s='IR')

# plotting data
ax.plot (wavelength * 10**6, bb_2000, \
         linestyle='-', linewidth=3, color='red', \
         label='Blackbody of T = 2000 K')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
