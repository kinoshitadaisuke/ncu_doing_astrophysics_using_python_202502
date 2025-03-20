#!/bin/sh

#
# Time-stamp: <2025/03/20 20:42:57 (UT+08:00) daisuke>
#

sqlite3 -header -column planet0.db "select name,mass,diameter,satellite, \
ring,magnetic_field from planet where mass > 1e+26 and diameter > 50000;"
