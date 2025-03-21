#!/bin/sh

#
# Time-stamp: <2025/03/20 22:41:07 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 bsc5.db ".schema --indent"
