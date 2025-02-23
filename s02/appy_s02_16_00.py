#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/08/02 14:50:52 (UT+8) daisuke>
#

# importing mpmath module
import mpmath

# settings for mpmath module
mpmath.mp.dps    = 100
mpmath.mp.pretty = True

# a function to calculate approximate value of pi
def new_pi (l, n):
    # initialising value of pi
    mp_1  = mpmath.mpf (1)
    mp_2  = mpmath.mpf (2)
    mp_4  = mpmath.mpf (4)
    mp_l  = mpmath.mpf (l)
    mp_pi = mp_4
    # calculating n terms
    for i in range (1, n+1):
        mp_i   = mpmath.mpf (i)
        a      = mp_1 / (mp_i + mp_l) - mp_4 / (mp_2 * mp_i + mp_1)
        b      = (mp_2 * mp_i + mp_1)**mp_2 / (mp_4 * (mp_i + mp_l) ) - mp_i
        c      = mp_i - mp_1
        d      = mpmath.factorial (i)
        mp_pi += a * mpmath.gamma (b + c) / mpmath.gamma (b) / d
    # returning calculated approximate value of pi
    return (mp_pi)

# calculation of approximate value of pi
l  = 10
n  = 10000000
pi = new_pi (l, n)

# printing result
print (f'approximate value of pi:')
print (f'100 digits:')
print (f'3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
print (f'new_pi ({l},{n}):')
print (f'{pi}')
