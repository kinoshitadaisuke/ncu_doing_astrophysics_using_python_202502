#!/bin/sh

#
# Time-stamp: <2025/03/20 20:52:36 (UT+08:00) daisuke>
#

sqlite3 dwarf_planet.db ".import --csv --skip 16 dwarf_planet.csv dwarfplanet"
