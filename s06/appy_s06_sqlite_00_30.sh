#!/bin/sh

#
# Time-stamp: <2025/03/20 20:56:58 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db "select name, a, e, i, H \
from dwarfplanet order by H;"
