#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/15 21:54:04 (UT+8) daisuke>
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
