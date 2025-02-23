#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 10:13:17 (UT+8) daisuke>
#

# importing os module
import os

# getting the name of the operating system
os_info = os.uname ()

# printing system information
print (f'about this system:')
print (f'  architecture = {os_info.machine}')
print (f'  OS name      = {os_info.sysname}')
print (f'  version      = {os_info.release}')
