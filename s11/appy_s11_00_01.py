#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/09 11:44:34 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

#
# command-line argument analysis
#

# constructing parser object
desc   = f"availability check of Python modules"
parser = argparse.ArgumentParser (description=desc)

# adding options
parser.add_argument ('module', type=str, nargs='+', \
                     help=f"module name (e.g. astropy)")

# analysis of command-line arguments
args = parser.parse_args ()

#
# input parameters
#

# list of module names for availability check
list_modules = args.module

#
# availability check of modules
#

for module in list_modules:
    # check of availability of module
    try:
        # importing module
        imported = __import__ (module)
    except:
        # if module is not installed, print an error message
        print (f"The module '{module}' is NOT installed on your computer.")
    else:
        # if module is found, print following message
        print (f"The module '{module}' is found on your computer.")
        print (f"{imported}")
    finally:
        # print that the check of availability of module is finished
        print (f"An availability check of '{module}' module is now finished.")
        print (f"")
