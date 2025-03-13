#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:09:47 (UT+08:00) daisuke>
#

# importing scipy module
import scipy.constants

# searching constants
search_result = scipy.constants.find ('light')

# printing search result
for constant in search_result:
    print (f'{constant}:')
    print (f'  value = {scipy.constants.value (constant)}')
    print (f'  error = {scipy.constants.precision (constant)}')
    print (f'  unit  = {scipy.constants.unit (constant)}')
