#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/21 09:08:07 (UT+08:00) daisuke>
#

# importing sqlite module
import sqlite3

# importing contextlib module
import contextlib

# database file name
file_db = 'ngc2000.db'

# SQL command for making a table
sql_maketable = f'create table ngc2000 (id text primary key, type text, ' \
    + f'ra text, dec text, constellation text, size real, mag real);'

# opening a connection to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # making a table
    cursor.execute (sql_maketable)

    # committing transaction
    conn.commit ()
