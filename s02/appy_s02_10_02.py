#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/26 00:09:46 (CST) daisuke>
#

# importing math module
import math

# two floats "a" and "b"
a = 12.34
b = -56.78

# ceil
a_ceil = math.ceil (a)
b_ceil = math.ceil (b)

# printing results
print (f'Use of ceil () function:')
print (f'  a         = {a}')
print (f'  ceil (a)  = {a_ceil}')
print (f'  {a_ceil} is the smallest integer greater than or equal to {a}.')
print (f'  b         = {b}')
print (f'  ceil (b)  = {b_ceil}')
print (f'  {b_ceil} is the smallest integer greater than or equal to {b}.')
print (f'')
