#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:41:49 (CST) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f(x)
func = 1 / sympy.sqrt (1/x - 1)

# integration of f(x) from x=0 to x=1
I = sympy.integrate (func, (x, 0, 1))

# printing result
print (f'I = {I}')
