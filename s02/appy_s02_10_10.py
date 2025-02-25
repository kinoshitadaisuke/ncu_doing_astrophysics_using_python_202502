#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/26 00:21:36 (CST) daisuke>
#

# importing math module
import math

# comb
c_5_3 = math.comb (5, 3)
c_8_4 = math.comb (8, 4)

fac_2 = math.factorial (2)
fac_3 = math.factorial (3)
fac_4 = math.factorial (4)
fac_5 = math.factorial (5)
fac_8 = math.factorial (8)

# printing results
print (f'Use of comb () function:')
print (f'  C (5, 3) = (5!) / (3! * 2!)')
print (f'           = {fac_5} / ({fac_3} * {fac_2})')
print (f'           = {c_5_3}')
print (f'  C (8, 4) = (8!) / (4! * 4!)')
print (f'           = {fac_8} / ({fac_4} * {fac_4})')
print (f'           = {c_8_4}')
print (f'')
