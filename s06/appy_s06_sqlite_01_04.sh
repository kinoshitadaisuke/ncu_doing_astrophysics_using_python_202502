#!/bin/sh

#
# Time-stamp: <2025/03/24 19:29:27 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column element.db \
	"select AtomicNumber, Name, Symbol, StandardState, Density \
	from element where Density >= 15.0 and Density != '' \
	order by Density desc;"
