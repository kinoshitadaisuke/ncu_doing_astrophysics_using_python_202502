#!/bin/sh

#
# Time-stamp: <2025/03/24 19:20:45 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header planet0.db \
	".mode table" \
	"select name,mass,diameter,satellite,ring,magnetic_field from planet;"
