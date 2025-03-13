#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:10:51 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# giga
giga = scipy.constants.giga

# frequency of electromagnetic radiation
frequency = 115.0 * giga

# wavelength of electromagnetic radiation
wavelength = scipy.constants.nu2lambda (frequency)

# printing the result of conversion
print (f'{frequency:g} [Hz] ==> {wavelength:g} [m]')
