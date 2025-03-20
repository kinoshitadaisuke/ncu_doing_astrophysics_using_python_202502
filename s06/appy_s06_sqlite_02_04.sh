#!/bin/sh

#
# Time-stamp: <2025/03/20 22:44:53 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column bsc5.db "select hr, name, ra_str, dec_str, \
glon, glat, vmag from bsc where glat > 85.0 order by glat desc;"
