#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:39:33 (CST) daisuke>
#

# importing sympy module
import sympy

# variable x
x, a, b, c = sympy.symbols ('x a b c')

# function f
f = a * x**2 + b * x + c

# solving f(x) = 0
sol = sympy.solve (f, x)

# printing result
print (f'solution of {f}=0:')
print (f'x = {sol}')
