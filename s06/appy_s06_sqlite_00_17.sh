#!/bin/sh

#
# Time-stamp: <2025/03/24 19:20:22 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header -column planet0.db \
	"select name,mass,diameter,satellite, ring,magnetic_field from planet;"
