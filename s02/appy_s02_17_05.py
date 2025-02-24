#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:39:53 (CST) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = sympy.sin (x)

# differentiation of f(x)
df_dx = sympy.diff (f, x)

# printing result
print (f'f(x)  = {f}')
print (f'df/dx = {df_dx}')
