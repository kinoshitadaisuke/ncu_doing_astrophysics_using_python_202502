#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:47:10 (UT+08:00) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'bsc/bsc5-all.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing information of stars brighter than 1.5 mag
print (f'# HR number, RA, Dec, Vmag, B-V, sptype')
for i in range (len (data)):
    if (float (data[i]['Vmag']) < 1.5):
        RA = f'{data[i]["RAh"]}h{data[i]["RAm"]}m{data[i]["RAs"]}s'
        Dec = f'{data[i]["DE-"]}{data[i]["DEd"]}d{data[i]["DEm"]}m{data[i]["DEs"]}s'
        print (f'{data[i]["HR"]:>5s}  {RA}  {Dec}', \
               f' {float (data[i]["Vmag"]):+5.2f}', \
               f' {float (data[i]["B-V"]):+5.2f}', \
               f' {data[i]["SpType"]}')
