#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 13:12:11 (UT+8) daisuke>
#

# importing os module
import os

# getting a list of files and directory
list_files1 = os.scandir ()

# printing list of files and directory
print (f'files and directories:')
for obj in list_files1:
    print (f'  {obj.name}')
    print (f'    is_dir = {obj.is_dir ()}')
    print (f'    mode   = {oct (obj.stat ().st_mode)}')

# directory name
dir_new = 'mynewdir'

# changing file mode
#   7 = 2^0 + 2^1 + 2^2 = 1 + 2 + 4 ==> read, write, execute are allowed
#   5 = 2^0       + 2^2 = 1 + 4     ==> read, execute are allowed
#   0                               ==> read, write, execute are not allowed
os.chmod (dir_new, 0o750)

# getting a list of files and directory
list_files2 = os.scandir ()

# printing list of files and directory
print (f'files and directories:')
for obj in list_files2:
    print (f'  {obj.name}')
    print (f'    is_dir = {obj.is_dir ()}')
    print (f'    mode   = {oct (obj.stat ().st_mode)}')
