#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/16 13:18:46 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy

# input data file name
file_input = 'appy_s05_10_00.data'

# making empty lists for storing data
list_x     = []
list_x_err = []
list_y     = []
list_y_err = []

# opening data file for reading
with open (file_input, 'r') as fh_r:
    # reading file line-by-line
    for line in fh_r:
        # skip if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting data
        (x_str, x_err_str, y_str, y_err_str) = line.split ()
        # converting string into float
        x     = float (x_str)
        x_err = float (x_err_str)
        y     = float (y_str)
        y_err = float (y_err_str)
        # appending data to the end of lists
        list_x.append (x)
        list_x_err.append (x_err)
        list_y.append (y)
        list_y_err.append (y_err)

# making numpy arrays
array_x    = numpy.array (list_x)
array_xerr = numpy.array (list_x_err)
array_y    = numpy.array (list_y)
array_yerr = numpy.array (list_y_err)

#
# fitting using ODR
#

# initial guess of coefficients
initial_guess = [1.0, 1.0]

# function for fitting
def func (coeff, x):
    y = coeff[0] * x + coeff[1]
    return (y)

# making a model for ODR
odr_model = scipy.odr.Model (func)

# making data for ODR
odr_data = scipy.odr.Data (array_x, array_y, \
                           wd=1.0/(array_xerr**2), we=1.0/(array_yerr**2))

# making ODR object for fitting
odr_fitting = scipy.odr.ODR (odr_data, odr_model, beta0=initial_guess)

# carrying out ODR fitting
odr_result = odr_fitting.run ()

# printing result of ODR fitting
print (odr_result.pprint ())

# printing fitted coefficients and their errors
print (f'')
print (f'fitted coefficients')
print (f'  a = {odr_result.beta[0]:8.3f} +/- {odr_result.sd_beta[0]:8.3f}')
print (f'  b = {odr_result.beta[1]:8.3f} +/- {odr_result.sd_beta[1]:8.3f}')
