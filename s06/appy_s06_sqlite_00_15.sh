#!/bin/sh

#
# Time-stamp: <2025/03/24 19:36:53 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header planet0.db \
	"select name,mass,diameter,satellite from planet;"
