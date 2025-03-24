#!/bin/sh

#
# Time-stamp: <2025/03/24 19:31:13 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column bsc5.db \
	"select hr, name, glon, glat, vmag, bv, sptype from bsc \
	where sptype like '%O%V%' and sptype not like '%O%IV%' order by glat;"
