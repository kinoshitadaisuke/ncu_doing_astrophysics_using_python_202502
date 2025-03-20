#!/bin/sh

#
# Time-stamp: <2025/03/20 20:55:51 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db "select * from dwarfplanet;"
