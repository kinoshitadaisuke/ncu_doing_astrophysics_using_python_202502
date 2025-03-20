#!/bin/sh

#
# Time-stamp: <2025/03/20 20:29:11 (UT+08:00) daisuke>
#

sqlite3 -header planet0.db "select name,mass,diameter,satellite from planet;"
