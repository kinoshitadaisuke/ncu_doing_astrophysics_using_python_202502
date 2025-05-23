#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/24 14:43:57 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing astroquery module
import astroquery.esa.hubble

# construction of parser object for argparse
descr  = 'listing HST data products'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('obsid', nargs='+', help='observation ID for HST data')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
list_obsid = args.obsid

# making esahubble object
esahubble = astroquery.esa.hubble.ESAHubble ()

# processing obs ID one-by-one
for obsid in list_obsid:
    # getting data product list
    table = esahubble.get_associated_files(observation_id=obsid)
    # printing result
    print (f'# obs. ID = {obsid}')
    print (table)
    print (f'')
    
