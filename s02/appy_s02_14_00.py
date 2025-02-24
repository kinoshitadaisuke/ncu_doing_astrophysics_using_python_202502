#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:36:28 (CST) daisuke>
#

# importing uncertainties module
import uncertainties

# quantity "a": 6.0 +/- 0.3
a = uncertainties.ufloat (6.0, 0.3)

# quantity "b": 9.0 +/- 0.4
b = uncertainties.ufloat (9.0, 0.4)

# calculation of a + b
c = a + b

# printing value of "c"
print (f'a = {a}')
print (f'b = {b}')
print (f'c = a + b = {a} + {b} = {c}')
