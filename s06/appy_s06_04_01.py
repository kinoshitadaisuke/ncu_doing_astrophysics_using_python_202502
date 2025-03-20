#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/20 23:49:17 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# catalogue file name
file_catalogue = 'mpcorb.data.gz'

# output file name
file_output = 'mpcorb_extracted.data'

# opening output file for writing
with open (file_output, 'w') as fh_w:
    # opening catalogue file for reading
    with gzip.open (file_catalogue, 'rb') as fh_r:
        # reading catalogue line-by-line
        for line in fh_r:
            # number of provisional designation
            try:
                designation = line[0:7].strip ().decode ('utf-8')
            except:
                continue
            # absolute magnitude
            try:
                absmag = float (line[8:13])
            except:
                absmag = -999.99
            # mean anomaly
            try:
                M = float (line[26:35])
            except:
                M = -999.99
            # argument of perihelion
            try:
                peri = float (line[37:46])
            except:
                peri = -999.99
            # longitude of ascending node
            try:
                node = float (line[48:57])
            except:
                node = -999.99
            # inclination
            try:
                i = float (line[59:68])
            except:
                i = -999.99
            # eccentricity
            try:
                e = float (line[70:79])
            except:
                e = -999.99
            # semimajor axis
            try:
                a = float (line[92:103])
            except:
                a = -999.99
            # number of observations
            try:
                nobs = int (line[117:122])
            except:
                nobs = -999
            # residual
            try:
                residual = float (line[137:141])
            except:
                residual = -999.99
            # 4-hexdigit flags
            try:
                flag = line[161:165].strip ().decode ('utf-8')
            except:
                flag = '9999'
            # readable name
            try:
                name = line[166:194].strip ().decode ('utf-8')
            except:
                name = '__NONE__'
            # last observation date
            try:
                lastobs = int (line[194:202])
            except:
                lastobs = 99999999

            # skip when reading the header
            if ( (a < -999.0) and (e < -999.0) and (i < -999.0) \
                 and (peri < -999.0) and (node < -999.0) and (M < -999.0) ):
                continue

            # writing extracted data to output file
            fh_w.write (f'designation = {designation}\n')
            fh_w.write (f'  name     = {name}\n')
            fh_w.write (f'  absmag   = {absmag}\n')
            fh_w.write (f'  M        = {M}\n')
            fh_w.write (f'  peri     = {peri}\n')
            fh_w.write (f'  node     = {node}\n')
            fh_w.write (f'  i        = {i}\n')
            fh_w.write (f'  e        = {e}\n')
            fh_w.write (f'  a        = {a}\n')
            fh_w.write (f'  nobs     = {nobs}\n')
            fh_w.write (f'  residual = {residual}\n')
            fh_w.write (f'  flag     = {flag}\n')
            fh_w.write (f'  lastobs  = {lastobs}\n')
