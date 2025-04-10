#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/21 00:01:09 (UT+08:00) daisuke>
#

# importing sqlite module
import sqlite3

# importing contextlib module
import contextlib

# database file name
file_db = 'mpcorb.db'

# connecting to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # SQL command for a query
    sql_query = 'select name, a, e, i, node, peri, M, nobs, residual, ' \
        + f'flag, lastobs, absmag from mpcorb ' \
        + f'where (a >= 1000.0) order by a desc;'

    # executing a SQL query
    cursor.execute (sql_query)

    # fetching results of query
    results = cursor.fetchall ()

    # printing results of query
    print (f'# name, a, e, i, node, peri, M, absmag')
    for result in results:
        print (f'{result[0]:24s}  {result[1]:8.2f}  {result[2]:5.3f} ', \
               f'{result[3]:6.2f} {result[4]:6.2f} {result[5]:6.2f} ', \
               f'{result[6]:6.2f}  {result[11]:7.2f}')
