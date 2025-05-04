#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:35:59 (UT+08:00) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'exoplanets/data/exoplanet.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing keys of the data
for key in data[0].keys ():
    print (f"{key}")
