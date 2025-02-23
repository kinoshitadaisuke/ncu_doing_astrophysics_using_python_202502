#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 20:48:32 (UT+8) daisuke>
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
