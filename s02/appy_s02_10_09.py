#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/26 00:19:34 (CST) daisuke>
#

# importing math module
import math

# perm
p_5_3 = math.perm (5, 3)
p_8_4 = math.perm (8, 4)

fac_2 = math.factorial (2)
fac_4 = math.factorial (4)
fac_5 = math.factorial (5)
fac_8 = math.factorial (8)

# printing results
print (f'Use of perm () function:')
print (f'  P (5, 3) = (5!) / (2!)')
print (f'           = {fac_5} / {fac_2}')
print (f'           = {p_5_3}')
print (f'  P (8, 4) = (8!) / (4!)')
print (f'           = {fac_8} / {fac_4}')
print (f'           = {p_8_4}')
print (f'')
