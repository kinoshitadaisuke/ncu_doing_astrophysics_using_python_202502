#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 10:05:48 (UT+8) daisuke>
#

# importing os module
import os

# obtaining the value of environmental variable "LANG"
env_lang = os.environ['LANG']

# printing the value of environmental variable "LANG"
print (f'LANG = {env_lang}')
