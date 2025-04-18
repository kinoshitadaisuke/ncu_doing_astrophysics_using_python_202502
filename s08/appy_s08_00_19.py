#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/06 15:05:10 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'appy_s08_00_19.png'

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

# function to calculate Rayleigh-Jeans law
def rj_nu (frequency, T):
    # speed of light
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Rayleigh-Jeans law
    blackbody = 2.0 * frequency**2 * k[0] * T / c[0]**2

    # returning blackbody curve by Rayleigh-Jeans law
    return (blackbody)

# function to calculate Wien's law
def wi_nu (frequency, T):
    # speed of light
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Planck constant
    h = scipy.constants.physical_constants['Planck constant']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Wien's law
    blackbody = 2.0 * h[0] * frequency**3 / c[0]**2 \
        * numpy.exp (-h[0] * frequency / (k[0] * T) )

    # returning blackbody curve by Wien's law
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
rj_5800 = rj_nu (frequency, T)
wi_5800 = wi_nu (frequency, T)

# printing Planck function
print (f'Frequency:')
print (f'{frequency}')
print (f'Planck function:')
print (f'{bb_5800}')
print (f'Rayleigh-Jeans law:')
print (f'{rj_5800}')
print (f'Wien\'s law:')
print (f'{wi_5800}')

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

# showing X-ray region
ax.fill_between ([3*10**16, 10**18], 10**-30, 10**-3, \
                 color='cyan', alpha=0.1)
ax.text (x=4*10**16, y=10**-29, s='X-ray')

# showing UV region
ax.fill_between ([10**15, 3*10**16], 10**-30, 10**-3, \
                 color='violet', alpha=0.1)
ax.text (x=1.1*10**15, y=10**-29, s='UV')

# showing visible region
ax.fill_between ([3*10**14, 10**15], 10**-30, 10**-3, \
                 color='green', alpha=0.1)
ax.text (x=10**14, y=3*10**-28, s='Visible')

# showing IR region
ax.fill_between ([10**12, 3*10**14], 10**-30, 10**-3, \
                 color='red', alpha=0.1)
ax.text (x=10**13, y=10**-29, s='IR')

# showing radio region
ax.fill_between ([10**0, 10**12], 10**-30, 10**-3, color='yellow', alpha=0.1)
ax.text (x=10**8, y=10**-29, s='Radio')

# plotting data
ax.plot (frequency, bb_5800, \
         linestyle='-', linewidth=5, color='red', \
         zorder=0.1, \
         label='Blackbody of T = 5800 K')
ax.plot (frequency, rj_5800, \
         linestyle='--', linewidth=3, color='blue', \
         zorder=0.2, \
         label='Rayleigh-Jeans law for T = 5800 K')
ax.plot (frequency, wi_5800, \
         linestyle=':', linewidth=3, color='green', \
         zorder=0.3, \
         label='Wien\'s law for T = 5800 K')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
