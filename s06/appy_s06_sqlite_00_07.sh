#!/bin/sh

#
# Time-stamp: <2025/03/20 20:19:17 (UT+08:00) daisuke>
#

sqlite3 planet0.db "insert into planet values ('Earth', 5.97E24, \
1.2756E4, 23.9, 365.2, 15, 1, 'No', 'Yes');"
