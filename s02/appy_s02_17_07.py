#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:40:14 (CST) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = x**2

# integration of f(x)
I = sympy.integrate (f, x)

# printing result
print (f'f(x)  = {f}')
print (f'integration of f(x) = {I}')
