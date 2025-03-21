#!/bin/sh

#
# Time-stamp: <2025/03/20 20:04:08 (UT+08:00) daisuke>
#

sqlite3 planet0.db "create table planet (name text primary key, \
mass real, diameter real, rotation_period real, orbital_period real, \
mean_temperature real, satellite integer, ring text, magnetic_field text);"
