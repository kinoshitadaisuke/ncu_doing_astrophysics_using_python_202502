#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/23 20:25:56 (CST) daisuke>
#

# importing os module
import os

# target file
file_target = '/etc/fstab'

# file information
stat = os.stat (file_target)

# printing file information
print (f'status of file "{file_target}":')
print (f'  file owner UID  = {stat.st_uid}')
print (f'  file owner GID  = {stat.st_gid}')
print (f'  file mode       = {oct (stat.st_mode)}')
print (f'  file size       = {stat.st_size} byte')
print (f'  number of links = {stat.st_nlink}')
