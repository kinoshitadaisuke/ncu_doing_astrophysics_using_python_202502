#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/20 09:59:49 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

#
# command-line argument analysis
#

# constructing parser object
descr  = f"existence check of files"
parser = argparse.ArgumentParser (description=descr)

# adding options
parser.add_argument ('files', type=str, nargs='+', \
                     help=f"files for existence check")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
list_files = args.files

#
# existence check of files
#

# processing each file
for filename in list_files:
    # making pathlib object
    path_file = pathlib.Path (filename)
    # existence check
    existence = path_file.exists ()
    # printing result
    if (existence):
        print (f"the file '{filename}' exists!")
    else:
        print (f"the file '{filename}' does NOT exist!")
