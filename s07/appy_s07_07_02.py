#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/05 11:25:32 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.modeling

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# input file name
file_input = 'synthetic_00.data'

# output file name
file_output = 'appy_s07_07_02.png'

# making empty lists for storing data
list_x = []
list_y = []

# opening data file
with open (file_input, 'r') as fh_r:
    # reading data file line-by-line
    for line in fh_r:
        # skipping if line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (x_str, y_str) = line.split ()
        # converting string into float
        try:
            x = float (x_str)
        except:
            continue
        try:
            y = float (y_str)
        except:
            continue
        # appending data to lists
        list_x.append (x)
        list_y.append (y)


# making numpy arrays
array_x = numpy.array (list_x)
array_y = numpy.array (list_y)

# initialisation of fitter
fitter = astropy.modeling.fitting.LevMarLSQFitter (calc_uncertainties=True)

# model used for fitting
model_linear = astropy.modeling.models.Linear1D ()

# carrying out a fitting
fitted_func = fitter (model_linear, array_x, array_y)

# degree of freedom
dof = len (array_x) - 2
print (f'dof = {dof}')

# calculation of reduced chi square
chi_square = sum ( (fitted_func (array_x) - array_y)**2 )
reduced_chi_square = chi_square / dof
print (f'chi square = {chi_square}')
print (f'reduced chi square = {reduced_chi_square}')

# fitted parameters
a = fitted_func.slope.value
b = fitted_func.intercept.value
a_err = (fitter.fit_info['param_cov'][0,0])**0.5
b_err = (fitter.fit_info['param_cov'][1,1])**0.5
print (f'a = {a:8.5f} +/- {a_err:8.5f}')
print (f'b = {b:8.5f} +/- {b_err:8.5f}')

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# plotting data points
ax.plot (array_x, array_y, \
         linestyle='None', marker='o', markersize=3, color='blue', \
         label='synthetic data points')

# plotting fitted line
fitted_x = numpy.linspace (0.0, 50.0, 10000)
fitted_y = fitted_func (fitted_x)
ax.plot (fitted_x, fitted_y, \
         linestyle=':', color='red', linewidth=2, \
         label='fitted line')

# axes
ax.legend ()
ax.grid ()
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# saving plot into file
fig.savefig (file_output, dpi=150)
