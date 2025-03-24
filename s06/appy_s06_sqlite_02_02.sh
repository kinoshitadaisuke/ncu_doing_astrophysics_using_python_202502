#!/bin/sh

#
# Time-stamp: <2025/03/24 19:30:20 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column bsc5.db \
	"select hr, name, ra_str, dec_str, vmag, sptype from bsc \
	where vmag < 1.5 and vmag > -50 order by vmag;"
