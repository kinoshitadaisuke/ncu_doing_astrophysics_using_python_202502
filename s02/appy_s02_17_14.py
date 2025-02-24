#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:41:28 (CST) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
f = sympy.exp (-x**2)

# positive infinity
pinf = sympy.oo

# negative infinity
ninf = -sympy.oo

# integration of f(x)
I = sympy.integrate (f, (x, ninf, pinf))

# printing result
print (f'I = {I}')
