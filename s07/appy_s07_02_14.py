#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/01 14:03:28 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.table

# VOTable file
file_vot = 'exoplanet.vot'

# reading VOTable file and making an Astropy table
table_exoplanet = astropy.table.Table.read (file_vot)

# printing information of planet discovered by direct imaging in 2023
mask = (table_exoplanet["detection_type"] == "Imaging") \
    & (table_exoplanet["discovered"] == 2023)
print (table_exoplanet[mask]["name", "mass", "semi_major_axis", \
                             "orbital_period", "detection_type", \
                             "discovered"])
