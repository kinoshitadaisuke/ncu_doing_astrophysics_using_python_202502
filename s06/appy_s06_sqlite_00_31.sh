#!/bin/sh

#
# Time-stamp: <2025/03/24 19:25:21 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db \
	"select name, a, e, i, perihelion, aphelion from dwarfplanet \
	order by aphelion desc;"
