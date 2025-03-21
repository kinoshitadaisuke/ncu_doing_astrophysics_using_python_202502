#!/bin/sh

#
# Time-stamp: <2025/03/20 23:11:27 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 hip.db ".schema --indent"
