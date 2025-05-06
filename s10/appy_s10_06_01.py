#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 12:57:35 (UT+08:00) daisuke>
#

# importing pathlib module
import pathlib

# list of data files
files = pathlib.Path ('.').glob ('osc_0000_1989/*.json')

# printing file names
for file in sorted (files):
    print (file)
