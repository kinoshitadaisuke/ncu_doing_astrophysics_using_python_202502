#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/07 15:54:49 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# constructing a parser object
descr  = 'opening a file, reading data, and storing data in a list'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('file', default='', help='input data file name')

# parsing arguments
args = parser.parse_args ()

# parameters
file_input = args.file

# making a pathlib object for input file
path_input = pathlib.Path (file_input)

# check of existence of input file
if not (path_input.exists ()):
    # printing a message
    print (f'ERROR: input file "{file_input}" does not exist!')
    # stopping the script
    sys.exit (0)

# making an empty list for storing data
list_data = []
    
# opening file
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # reading data
        data_str = line
        # conversion from string into float
        try:
            # conversion from string into float
            data = float (data_str)
        except:
            # printing a message
            print (f'ERROR: conversion from string into float failed!')
            # stopping this script
            sys.exit (0)
        # appending data to the end of the list
        list_data.append (data)

# printing information of the list
print (f'number of data in the list = {len (list_data)}')
