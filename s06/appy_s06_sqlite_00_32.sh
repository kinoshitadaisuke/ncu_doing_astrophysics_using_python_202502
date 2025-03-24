#!/bin/sh

#
# Time-stamp: <2025/03/24 19:26:15 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column dwarf_planet.db \
	"select * from dwarfplanet where P > 300;"
