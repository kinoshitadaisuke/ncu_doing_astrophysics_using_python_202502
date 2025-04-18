#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/04 20:04:56 (CST) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of a resource
url_pi3 = 'https://s3b.astro.ncu.edu.tw/appy_202502/data/numpy_00.data'

# output file name
file_output = 'numpy_00.data'

# printing status
print (f'Now, opening {url_pi3}...')

# opening URL
with urllib.request.urlopen (url_pi3) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Retrieved data from {url_pi3}!')
    
# converting raw byte data into string
data_str = data_byte.decode ('utf-8')

# printing status
print (f'Now, writing data to file "{file_output}"...')

# opening file for writing
with open (file_output, 'w') as fh_write:
    # writing data into file
    fh_write.write (data_str)

# printing status
print (f'Finished writing data to file "{file_output}"!')
