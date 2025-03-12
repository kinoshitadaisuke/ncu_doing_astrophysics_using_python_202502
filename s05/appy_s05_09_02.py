#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/08 23:27:04 (UT+8) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.special

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'appy_s05_09_02.png'

# values of x
array_x = numpy.linspace (-6.0, +6.0, 20001)

# calculation of gamma function
array_y = scipy.special.gamma (array_x)

# printing (x, y)
print (f'array_x:')
print (f'{array_x}')
print (f'array_y:')
print (f'{array_y}')

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('X')
ax.set_ylabel ('Y')
ax.grid ()
ax.set_ylim (-50.0, +50.0)

# plotting data
ax.plot (array_x, array_y, \
         linestyle='-', linewidth=3, color='red', \
         label='gamma function')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=100)
