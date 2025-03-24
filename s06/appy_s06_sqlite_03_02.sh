#!/bin/sh

#
# Time-stamp: <2025/03/24 19:31:44 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column hip.db \
	"select hip, ra_hms, dec_dms, vmag, bv, parallax, sptype from hip \
	where hip <= 10 order by hip;"
