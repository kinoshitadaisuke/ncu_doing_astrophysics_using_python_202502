#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 12:58:35 (UT+08:00) daisuke>
#

# importing json module
import json

# file name
file_json = 'osc_0000_1989/SN1989V.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON data from file
    data = json.load (fh)

# printing data
for obj in data:
    print ("obj =", obj)
    for key in data[obj]:
        print ("  %-16s ==> %s" % (key, data[obj][key]) )
