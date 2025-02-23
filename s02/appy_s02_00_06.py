#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/23 20:26:10 (CST) daisuke>
#

# importing os module
import os

# obtaining the value of environmental variable "LANG"
env_lang = os.environ['LANG']

# printing the value of environmental variable "LANG"
print (f'LANG = {env_lang}')
