#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/25 11:54:30 (CST) daisuke>
#

# importing os module
import os

# target directory
dir_target = '/usr/share/locale'

# obtaining a list of files and directories at the directory "dir_target"
list_files = os.scandir (path=dir_target)

# printing files and directories
print (f'list of files and directories at "{dir_target}":')
# for each file (or directory) in the list
for filename in list_files:
    # printing information of file (or directory)
    print (f'  {filename.name}')
    print (f'    path       = {filename.path}')
    print (f'    is_file    = {filename.is_file ()}')
    print (f'    is_dir     = {filename.is_dir ()}')
    print (f'    is_symlink = {filename.is_symlink ()}')
    print (f'    mode       = {oct (filename.stat ().st_mode)}')
    print (f'    size       = {filename.stat ().st_size} byte')
        
