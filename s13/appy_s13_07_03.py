#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/24 14:44:35 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing astroquery module
import astroquery.esa.hubble

# construction of parser object for argparse
descr  = 'downloading HST data'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('files', nargs='+', help='file name for HST data')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
list_files = args.files

# making esahubble object
esahubble = astroquery.esa.hubble.ESAHubble ()

# downloading file one-by-one
for file_data in list_files:
    esahubble.download_file (file=file_data)
