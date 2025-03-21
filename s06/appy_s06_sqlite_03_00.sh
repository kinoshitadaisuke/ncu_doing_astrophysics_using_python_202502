#!/bin/sh

#
# Time-stamp: <2025/03/20 23:10:08 (UT+08:00) daisuke>
#

# printing tables in the database file "hip.db"
sqlite3 hip.db ".tables"
