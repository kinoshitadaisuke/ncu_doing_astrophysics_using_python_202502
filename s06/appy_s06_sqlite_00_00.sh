#!/bin/sh

#
# Time-stamp: <2025/03/24 19:33:41 (UT+08:00) daisuke>
#

# making a table
sqlite3 planet0.db \
	"create table planet (name text primary key, \
	mass real, diameter real, rotation_period real, orbital_period real, \
	mean_temperature real, satellite integer, ring text, \
	magnetic_field text);"
