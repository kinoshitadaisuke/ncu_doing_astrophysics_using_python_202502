#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:22:43 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.units

# units
u_m         = astropy.units.m
u_kg        = astropy.units.kg
u_kg_per_m3 = u_kg / u_m**3

# density in kg/m^3
rho_si = 3000.0 * u_kg_per_m3

# density in g/cm^3
rho_cgi = rho_si.cgs

# printing density in SI and in CGS
print (f'rho = {rho_si}')
print (f'    = {rho_cgi}')
