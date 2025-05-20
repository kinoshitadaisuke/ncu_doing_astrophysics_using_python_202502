#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/20 09:58:18 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

#
# command-line argument analysis
#

# constructing parser object
descr  = f"Adding two integers"
parser = argparse.ArgumentParser (description=descr)

# adding options
parser.add_argument ('-a', type=int, default=1, help=f"integer 1 (default: 1)")
parser.add_argument ('-b', type=int, default=2, help=f"integer 2 (default: 2)")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
a = args.a
b = args.b

#
# calculation
#

# calculation of adding two integers
c = a + b

# printing result
print (f"a = {a}")
print (f"b = {b}")
print (f"c = a + b = {c}")
