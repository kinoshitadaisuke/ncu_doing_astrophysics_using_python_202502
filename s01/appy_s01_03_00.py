#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/18 22:40:00 (CST) daisuke>
#

# defining a function to calculate a square of given number
def calc_square (a):
    # calculation of a square of given number
    sq = a**2
    # returning result of calculation
    return (sq)

# a number
x = 9

# using the function "calc_square ()"
sq_x = calc_square (x)

# printing result of calculation
print (f'x    = {x}')
print (f'x**2 = {x}**2 = {sq_x}')
