#!/bin/sh

#
# Time-stamp: <2025/03/20 20:28:16 (UT+08:00) daisuke>
#

sqlite3 -header planet0.db "select * from planet;"
