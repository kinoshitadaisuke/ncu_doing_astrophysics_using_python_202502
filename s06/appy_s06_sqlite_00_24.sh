#!/bin/sh

#
# Time-stamp: <2025/03/20 20:48:08 (UT+08:00) daisuke>
#

sqlite3 dwarf_planet.db "create table dwarfplanet (name text primary key, \
a real, e real, i real, perihelion real, aphelion real, P real, H real);"
