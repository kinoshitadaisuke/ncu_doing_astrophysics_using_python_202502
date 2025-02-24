#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:39:16 (CST) daisuke>
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
