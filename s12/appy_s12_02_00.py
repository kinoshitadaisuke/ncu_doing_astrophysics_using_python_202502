#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/12/04 11:47:15 (UT+8) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_data = 'https://iopscience.iop.org/article/10.1086/339557/fulltext/201498.tb2.txt?doi=10.1086/339557'

# output file name
file_output = '201498.tb2.txt'

# printing status
print (f'Now, fetching {url_data}...')

# making request object
req = urllib.request.Request (url_data)
req.add_header ('Referer', 'https://iopscience.iop.org/article/10.1086/339557/fulltext/')
req.add_header ('User-Agent', 'Mozilla/5.0 (X11; NetBSD x86_64; rv:128.0) Gecko/20100101 Firefox/128.0')

# opening URL
with urllib.request.urlopen (req) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Finished fetching {url_data}!')

# printing status
print (f'Now, writing data into file "{file_output}"...')

# opening file for writing
with open (file_output, 'wb') as fh_write:
    # writing data
    fh_write.write (data_byte)

# printing status
print (f'Finished writing data into file "{file_output}"!')
