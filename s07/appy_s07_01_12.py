#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:23:16 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.constants
import astropy.units

# units
u_kg          = astropy.units.kg
u_MeV         = astropy.units.MeV
u_J           = astropy.units.J
u_J_per_kg    = u_J / u_kg
u_mass_energy = astropy.units.mass_energy ()

# proton mass
m_p = astropy.constants.m_p

# atomic mass unit
amu = astropy.constants.u

# helium-4 nucleus mass
m_He4 = 4.002603254 * amu

# mass difference between 4 protons and 1 He-4 nucleus
m_diff = m_p * 4 - m_He4

# conversion from mass to energy
energy_MeV      = m_diff.to (u_MeV, equivalencies=u_mass_energy)
energy_J        = m_diff.to (u_J, equivalencies=u_mass_energy)
specific_energy = energy_J / (m_p * 4)

# printing result
print (f'Delta mass = {m_diff:g}  ==>  energy = {energy_MeV:g}')
print (f'specific energy = {specific_energy:g}')
