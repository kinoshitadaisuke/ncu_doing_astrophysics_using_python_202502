#!/bin/sh

#
# Time-stamp: <2025/03/20 21:14:19 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 element.db ".schema --indent"
