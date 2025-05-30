#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/20 22:33:35 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# importing sys module
import sys

# catalogue file name
file_catalogue = 'bsc5.data.gz'

# output file name
file_output = 'bsc5_extracted.data'

# opening output file for writing
with open (file_output, 'w') as fh_w:
    # opening catalogue file for reading
    with gzip.open (file_catalogue, 'rb') as fh_r:
        # reading catalogue line-by-line
        for line in fh_r:
            # Harvard Revised Number of star
            try:
                HR = int (line[0:4])
            except:
                # printing message
                print (f'ERROR: Something is wrong with following line...')
                print (f'ERROR:   {line[:75]}')
                print (f'ERROR: Cannot extract HR number!')
                # exit
                sys.exit (1)
            # name of star
            name = line[4:14].strip ().decode ('utf-8')
            if (name == ''):
                name = '__NONE__'
            # RA
            try:
                RA_h = int (line[75:77])
                RA_m = int (line[77:79])
                RA_s = float (line[79:83])
            except:
                RA_h = 99
                RA_m = 99
                RA_s = 99.9
            RA_str = f'{RA_h:02d}:{RA_m:02d}:{RA_s:04.1f}'
            RA_deg = (RA_h + RA_m / 60.0 + RA_s / 3600.0) * 15.0
            # Dec
            try:
                Dec_sign = line[83:84].decode ('utf-8')
                Dec_d    = int (line[84:86])
                Dec_m    = int (line[86:88])
                Dec_s    = int (line[88:90])
            except:
                Dec_sign = '-'
                Dec_d    = 99
                Dec_m    = 99
                Dec_s    = 99
            Dec_str = f'{Dec_sign}{Dec_d:02d}:{Dec_m:02d}:{Dec_s:02d}'
            if (Dec_sign == '+'):
                Dec_deg = Dec_d + Dec_m / 60.0 + Dec_s / 3600.0
            else:
                Dec_deg = (Dec_d + Dec_m / 60.0 + Dec_s / 3600.0) * (-1.0)
            # galactic longitude
            try:
                glon = float (line[90:96])
            except:
                glon = -999.99
            # galactic latitude
            try:
                glat = float (line[96:102])
            except:
                glat = -999.99
            # Vmag
            try:
                mag_V = float (line[102:107])
            except:
                mag_V = -999.9
            # B-V colour
            try:
                colour_BV = float (line[109:114])
            except:
                colour_BV = -999.9
            # spectral type
            sptype = line[127:147].strip ().decode ('utf-8')
            # proper motion RA
            try:
                pm_RA = float (line[148:154])
            except:
                pm_RA = -999.9
            # proper motion Dec
            try:
                pm_Dec = float (line[154:160])
            except:
                pm_Dec = -999.9
            # parallax
            try:
                parallax = float (line[161:166])
            except:
                parallax = -999.9

            # writing extracted data to output file
            fh_w.write (f'HR = {HR}\n')
            fh_w.write (f'  name     = "{name}"\n')
            fh_w.write (f'  RA_str   = {RA_str}\n')
            fh_w.write (f'  RA_deg   = {RA_deg}\n')
            fh_w.write (f'  Dec_str  = {Dec_str}\n')
            fh_w.write (f'  Dec_deg  = {Dec_deg}\n')
            fh_w.write (f'  glon     = {glon}\n')
            fh_w.write (f'  glat     = {glat}\n')
            fh_w.write (f'  Vmag     = {mag_V}\n')
            fh_w.write (f'  B-V      = {colour_BV}\n')
            fh_w.write (f'  sptype   = "{sptype}"\n')
            fh_w.write (f'  pmRA     = {pm_RA}\n')
            fh_w.write (f'  pmDec    = {pm_Dec}\n')
            fh_w.write (f'  parallax = {parallax}\n')
