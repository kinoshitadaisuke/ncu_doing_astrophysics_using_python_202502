#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:37:41 (CST) daisuke>
#

# importing uncertainties module
import uncertainties

# quantity "a": 8.0 +/- 0.8
a = uncertainties.ufloat (8.0, 0.8)

# quantity "b": 4.0 +/- 0.6
b = uncertainties.ufloat (4.0, 0.6)

# calculation of a / b
c = a / b

# printing value of "c"
print (f'a = {a}')
print (f'b = {b}')
print (f'c = a / b = {a} / {b} = {c}')
