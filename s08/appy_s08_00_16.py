#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/06 15:04:05 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'appy_s08_00_16.png'

# resolution in DPI
resolution_dpi = 150

#
# function to calculate blackbody curve
#
def bb_nu (frequency, T):
    # speed of light in vacuum
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Planck constant
    h = scipy.constants.physical_constants['Planck constant']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Planck function
    blackbody = 2.0 * h[0] * frequency**3 / c[0]**2 \
        / (numpy.exp (h[0] * frequency / (k[0] * T) ) - 1.0 )

    # returning blackbody radiation curve
    return (blackbody)

# temperature of blackbody
T = 5800.0

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T} K')

# range of frequency (from 10**2 Hz to 10**16 Hz)
frequency_min = 2.0
frequency_max = 16.0

# frequency in Hz
frequency = numpy.logspace (frequency_min, frequency_max, num=14001)

# T = 5800 K blackbody spectrum
bb_5800 = bb_nu (frequency, T)

# printing Planck function
print (f'Frequency:')
print (f'{frequency}')
print (f'Planck function:')
print (f'{bb_5800}')

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel (r'Frequency [Hz]')
ax.set_ylabel (r'Specific Intensity [W sr$^{-1}$ m$^{-2}$ Hz$^{-1}$]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (10**2, 10**17)
ax.set_ylim (10**-30, 10**-3)

# make secondary X-axis
c   = scipy.constants.physical_constants['speed of light in vacuum'][0]
ax2 = ax.secondary_xaxis (location='top', \
                          functions=(lambda x: c/x, lambda x: c/x) )
ax2.set_xlabel (r'Wavelength [m]')

# plotting data
ax.plot (frequency, bb_5800, \
         linestyle='-', linewidth=3, color='red', \
         label='Blackbody of T = 5800 K')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
