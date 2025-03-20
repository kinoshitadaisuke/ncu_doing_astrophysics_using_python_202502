#!/bin/sh

#
# Time-stamp: <2025/03/20 22:36:59 (UT+08:00) daisuke>
#

# making a database
sqlite3 bsc5.db ".read bsc5_makedb.sql"
