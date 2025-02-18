#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/18 22:38:30 (CST) daisuke>
#

# two numbers
a, b = 23, 7

# calculation
quotient  = a // b
remainder = a % b

# printing result of calculation
print (f'a         = {a}')
print (f'b         = {b}')
print (f'quotient  = {quotient}')
print (f'remainder = {remainder}')
print (f'{b} * {quotient} + {remainder} = {b * quotient + remainder}')
