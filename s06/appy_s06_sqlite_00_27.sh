#!/bin/sh

#
# Time-stamp: <2025/03/24 19:24:10 (UT+08:00) daisuke>
#

# importing data from CSV file
sqlite3 dwarf_planet.db ".import --csv --skip 16 dwarf_planet.csv dwarfplanet"
