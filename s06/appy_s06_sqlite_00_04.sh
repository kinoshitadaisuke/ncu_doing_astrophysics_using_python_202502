#!/bin/sh

#
# Time-stamp: <2025/03/24 19:17:25 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 planet0.db ".schema --indent"
