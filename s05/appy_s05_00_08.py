#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:10:34 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# nano
nano = scipy.constants.nano

# wavelength of electromagnetic radiation
wavelength = 500.0 * nano

# frequency of electromagnetic radiation
frequency = scipy.constants.lambda2nu (wavelength)

# printing the result of conversion
print (f'{wavelength:g} [m] ==> {frequency:g} [Hz]')
