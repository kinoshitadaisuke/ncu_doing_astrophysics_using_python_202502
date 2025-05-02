#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/12 09:52:00 (UT+8) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'bsc/bsc5-all.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing keys of the data
for key in data[0].keys ():
    print (f"{key}")
