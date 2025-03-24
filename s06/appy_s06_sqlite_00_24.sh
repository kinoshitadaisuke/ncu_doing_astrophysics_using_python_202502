#!/bin/sh

#
# Time-stamp: <2025/03/24 19:23:24 (UT+08:00) daisuke>
#

# SQL query
sqlite3 dwarf_planet.db \
	"create table dwarfplanet (name text primary key, \
	a real, e real, i real, perihelion real, aphelion real, P real, H real);"
