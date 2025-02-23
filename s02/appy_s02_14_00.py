#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 17:40:46 (UT+8) daisuke>
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
