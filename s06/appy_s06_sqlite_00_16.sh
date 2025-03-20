#!/bin/sh

#
# Time-stamp: <2025/03/20 20:29:50 (UT+08:00) daisuke>
#

sqlite3 -header -column planet0.db "select name,mass,diameter,satellite from planet;"
