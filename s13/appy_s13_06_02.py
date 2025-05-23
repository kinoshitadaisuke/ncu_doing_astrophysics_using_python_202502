#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/24 13:59:38 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing datetime module
import datetime

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.esa.jwst

# date/time
now = datetime.datetime.now ().isoformat ()

# command name
command = sys.argv[0]

# constructing parser object
descr  = "getting data product list of JWST data"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--obsid', default='', \
                     help='observation ID of JWST data')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
obsid = args.obsid

# getting product list
product_list = astroquery.esa.jwst.Jwst.get_product_list (observation_id=obsid)

# printing product list
print (f'# file name, product type, calib. level, availability')
for i in range (len (product_list)):
    print (f'{product_list["filename"][i]:56s}', \
           f'{product_list["producttype"][i]:10s}', \
           f'{product_list["calibrationlevel"][i]:2d}', \
           f'{product_list["public"][i]}')
