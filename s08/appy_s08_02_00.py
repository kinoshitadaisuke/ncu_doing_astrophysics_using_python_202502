#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/12 20:29:15 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_data = 'https://www.nrel.gov/media/docs/libraries/grid/newguey2003.txt'

# output file name
file_output = 'solar_spec.data'

# printing status
print (f'Fetching {url_data}...')

# opening URL
request = urllib.request.Request (url_data)
request.add_header ('User-Agent', 'Mozilla/5.0 (X11; NetBSD x86_64; rv:128.0) Gecko/20100101 Firefox/128.0')
with urllib.request.urlopen (request) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Fetched {url_data}!')

# converting raw byte data into string
data_str = data_byte.decode ('utf-8')

# printing status
print (f'Now, writing data into file "{file_output}"...')

# opening file for writing
with open (file_output, 'w') as fh_write:
    # writing data
    fh_write.write (data_str)

# printing status
print (f'Finished writing data into file "{file_output}"!')
