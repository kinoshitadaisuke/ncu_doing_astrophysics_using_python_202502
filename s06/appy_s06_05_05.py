#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/15 22:18:31 (UT+8) daisuke>
#

# importing sqlite module
import sqlite3

# importing contextlib module
import contextlib

# database file name
file_db = 'ngc2000.db'

# connecting to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # SQL command for a query
    sql_query = 'select id,type,constellation,size,mag from ngc2000 ' \
        + f'where type is "galaxy" and size > 30 order by mag;'

    # executing a SQL query
    cursor.execute (sql_query)

    # fetching results of query
    results = cursor.fetchall ()

    # printing results of query
    print (f'# ID    Constellation Size (arcmin)    Mag  Object Type')
    for result in results:
        print (f'{result[0]:7s} {result[2]:>13s} {result[3]:13.1f}', \
               f' {result[4]:5.1f}  {result[1]}')
