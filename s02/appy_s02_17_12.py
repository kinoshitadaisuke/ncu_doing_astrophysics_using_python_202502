#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:41:08 (CST) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
f = -x + 1

# integration of f(x) from 0 to 1
I = sympy.integrate (f, (x, 0, 1))

# printing result
print (f'I = {I}')
