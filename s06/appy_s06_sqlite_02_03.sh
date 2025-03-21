#!/bin/sh

#
# Time-stamp: <2025/03/20 22:43:50 (UT+08:00) daisuke>
#

# SQL query
sqlite3 --header --column bsc5.db "select hr, name, ra_str, dec_str, \
vmag, bv, parallax from bsc where parallax >= 0.2 order by parallax desc;"
