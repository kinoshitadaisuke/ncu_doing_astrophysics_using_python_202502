#!/bin/sh

#
# Time-stamp: <2025/03/24 19:19:30 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -header planet0.db "select * from planet;"
