#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/26 09:24:27 (UT+08:00) daisuke>
#

# importing astropy module
import astropy.table

# VOTable file
file_vot = 'exoplanet.vot'

# reading VOTable file and making an Astropy table
table_exoplanet = astropy.table.Table.read (file_vot)

# printing information of planet "51 Peg b"
for i in range (len (table_exoplanet)):
    if (table_exoplanet[i]["name"] == "51 Peg b"):
        print (table_exoplanet[i]["name", "mass", "semi_major_axis", \
                                  "orbital_period", "detection_type", \
                                  "discovered"])
