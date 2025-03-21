#!/bin/sh

#
# Time-stamp: <2025/03/20 21:01:54 (UT+08:00) daisuke>
#

# exporting database
sqlite3 dwarf_planet.db ".dump" > dwarf_planet.sql
