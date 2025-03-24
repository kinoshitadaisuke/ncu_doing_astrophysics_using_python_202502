#!/bin/sh

#
# Time-stamp: <2025/03/24 19:23:37 (UT+08:00) daisuke>
#

# printing structure of table
sqlite3 dwarf_planet.db ".schema --indent"
