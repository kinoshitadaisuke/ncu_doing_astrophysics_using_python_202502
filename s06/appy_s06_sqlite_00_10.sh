#!/bin/sh

#
# Time-stamp: <2025/03/24 19:36:00 (UT+08:00) daisuke>
#

# adding data to table
sqlite3 planet0.db \
	"insert into planet values ('Saturn', 5.68E26, 1.20536E5, 10.7, \
	10747, -140, 82, 'Yes', 'Yes');"
