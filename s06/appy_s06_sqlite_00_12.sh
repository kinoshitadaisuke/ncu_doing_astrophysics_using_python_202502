#!/bin/sh

#
# Time-stamp: <2025/03/24 19:36:29 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Neptune', 1.02E26, 4.9528E4, 16.1, \
	59800, -200, 14, 'Yes', 'Yes');"
