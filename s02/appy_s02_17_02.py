#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/24 21:39:25 (CST) daisuke>
#

# importing sympy module
import sympy

# variable x
x = sympy.symbols ('x')

# function f
f = (1 + 1/x)**x

# limit x --> infinity
lim_f = sympy.limit (f, x, sympy.oo)

# printing result
print (f'lim x->infty [{f}] = {lim_f}')
