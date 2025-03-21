#!/bin/sh

#
# Time-stamp: <2025/03/20 21:15:39 (UT+08:00) daisuke>
#

# importing data from CSV file
sqlite3 element.db ".import --csv --skip 1 periodictable.csv element"
