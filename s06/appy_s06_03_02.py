#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/20 23:07:35 (UT+08:00) daisuke>
#

# importing sys module
import sys

# catalogue file name
file_catalogue = 'hip.cat'

# output file name
file_output = 'hip_extracted.data'

# opening output file for writing
with open (file_output, 'w') as fh_w:
    # opening catalogue file for reading
    with open (file_catalogue, 'r') as fh_r:
        # reading catalogue line-by-line
        for line in fh_r:
            # Hipparcos Number of star
            try:
                hip = int (line[8:14])
            except:
                # printing message
                print (f'ERROR: Something is wrong with following line...')
                print (f'ERROR:   {line[:75]}')
                print (f'ERROR: Cannot extract Hipparcos number!')
                # exit
                sys.exit (1)
            # RA in hhmmss format
            try:
                RA_hms = line[17:28].strip ()
            except:
                RA_hms = '99 99 99.99'
            # Dec in ddmmss format
            try:
                Dec_dms = line[29:40].strip ()
            except:
                Dec_dms = '-99 99 99.9'
            # V-band magnitude
            try:
                mag_V = float (line[41:46])
            except:
                mag_V = -99.99
            # RA in deg
            try:
                RA_deg = float (line[51:63])
            except:
                RA_deg = -999.99
            # Dec in deg
            try:
                Dec_deg = float (line[64:76])
            except:
                Dec_deg = -999.99
            # parallax in mas
            try:
                parallax = float (line[79:86])
            except:
                parallax = -999999.99
            # proper motion in RA
            try:
                pm_RA = float (line[87:95])
            except:
                pm_RA = -999999.99
            # proper motion in Dec
            try:
                pm_Dec = float (line[96:104])
            except:
                pm_Dec = -999999.99
            # (B-V) colour index
            try:
                colour_BV = float (line[245:251])
            except:
                colour_BV = -999.99
            # (V-I) colour index
            try:
                colour_VI = float (line[260:264])
            except:
                colour_VI = -999.99
            # spectral type
            try:
                sptype = line[435:447].strip ()
            except:
                sptype = '___NONE___'

            # writing extracted data to output file
            fh_w.write (f'HIP = {hip}\n')
            fh_w.write (f'  RA_hms   = "{RA_hms}"\n')
            fh_w.write (f'  RA_deg   = {RA_deg}\n')
            fh_w.write (f'  Dec_dms  = "{Dec_dms}"\n')
            fh_w.write (f'  Dec_deg  = {Dec_deg}\n')
            fh_w.write (f'  Vmag     = {mag_V}\n')
            fh_w.write (f'  B-V      = {colour_BV}\n')
            fh_w.write (f'  V-I      = {colour_VI}\n')
            fh_w.write (f'  parallax = {parallax}\n')
            fh_w.write (f'  pmRA     = {pm_RA}\n')
            fh_w.write (f'  pmDec    = {pm_Dec}\n')
            fh_w.write (f'  sptype   = "{sptype}"\n')
