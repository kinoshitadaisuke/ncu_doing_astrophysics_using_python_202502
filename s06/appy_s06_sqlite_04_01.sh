#!/bin/sh

#
# Time-stamp: <2025/03/20 23:58:48 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 mpcorb.db ".schema --indent"
