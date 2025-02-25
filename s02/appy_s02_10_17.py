#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/02/26 00:31:03 (CST) daisuke>
#

# importing math module
import math

# distance between two points
coord_0  = (0.0, 1.0)
coord_1  = (3.0, 2.0)
dist_0_1 = math.dist (coord_0, coord_1)
coord_2  = (0.0, 0.0, 0.0)
coord_3  = (1.0, 1.0, 1.0)
dist_2_3 = math.dist (coord_2, coord_3)

# printing result
print (f'coord_0 = {coord_0}')
print (f'coord_1 = {coord_1}')
print (f'distance between coord_0 and coord_1 = {dist_0_1}')
print (f'coord_2 = {coord_2}')
print (f'coord_3 = {coord_3}')
print (f'distance between coord_2 and coord_3 = {dist_2_3}')
