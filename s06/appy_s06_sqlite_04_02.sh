#!/bin/sh

#
# Time-stamp: <2025/03/24 19:32:29 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column mpcorb.db \
	"select designation,name,a,e,i,absmag from mpcorb \
	where absmag < 3 and absmag > -100 order by absmag;"
