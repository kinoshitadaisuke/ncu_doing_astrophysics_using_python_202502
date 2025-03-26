#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:22:47 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# units
u_cm        = astropy.units.cm
u_g         = astropy.units.g
u_g_per_cm3 = u_g / u_cm**3

# density in g/cm^3
rho_cgi = 3.0 * u_g_per_cm3

# density in kg/m^3
rho_si = rho_cgi.si

# printing density in SI and in CGS
print (f'rho = {rho_cgi}')
print (f'    = {rho_si}')
