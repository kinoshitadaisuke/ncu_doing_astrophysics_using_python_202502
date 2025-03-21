#!/bin/sh

#
# Time-stamp: <2025/03/20 20:35:31 (UT+08:00) daisuke>
#

sqlite3 -header planet0.db ".mode table" "select name,mass,diameter,\
satellite,ring,magnetic_field from planet;"
