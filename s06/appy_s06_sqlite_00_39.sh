#!/bin/sh

#
# Time-stamp: <2025/03/24 19:27:54 (UT+08:00) daisuke>
#

# exporting database into a CSV file
sqlite3 dwarf_planet3.db \
	".header on" \
	".mode csv" \
	".once new.csv" \
	"select * from dwarfplanet;"
