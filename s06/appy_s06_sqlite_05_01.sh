#!/bin/sh

#
# Time-stamp: <2025/03/21 09:18:14 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 ngc2000.db ".schema --indent"
