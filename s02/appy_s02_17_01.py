#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 20:48:28 (UT+8) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = x**2 + x - 2

# factorisation of f
f2 = sympy.factor (f)

# printing result
print (f'{f} = {f2}')
