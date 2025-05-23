#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/04/19 11:04:59 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# catalogue file
file_catalogue = 'bsc5.cat.gz'

# output file
file_output = 'bsc5.data'

# dictionary for storing data
bsc = {}

# opening file
with gzip.open (file_catalogue, 'rb') as fh_in:
    # reading the catalogue file line-by-line
    for line in fh_in:
        # decoding byte data
        line = line.decode ('utf-8')

        # finding values
        # Harvard Revised number
        hr_str = line[0:4].strip ()
        # RA_h
        RA_h_str = line[75:77].strip()
        # RA_m
        RA_m_str = line[77:79].strip()
        # RA_s
        RA_s_str = line[79:83].strip()
        # Dec_sign
        Dec_sign_str = line[83]
        # Dec_d
        Dec_d_str = line[84:86].strip ()
        # Dec_m
        Dec_m_str = line[86:88].strip ()
        # Dec_s
        Dec_s_str = line[88:90].strip ()
        # galactic longitude
        glon_str = line[90:96].strip ()
        # galactic latitude
        glat_str = line[96:102].strip ()
        # V-band magnitude
        Vmag_str = line[102:107].strip ()

        # skip processing, if any of necessary fields is blank.
        if ( (hr_str == '') or (RA_h_str == '') or (Dec_sign_str == '') 
             or (glon_str == '') or (Vmag_str == '') ):
            continue

        # HR number
        hr = int (hr_str)
        # RA
        RA_h = int (RA_h_str)
        RA_m = int (RA_m_str)
        RA_s = float (RA_s_str)
        RA = "%02d:%02d:%04.1f" % (RA_h, RA_m, RA_s)
        # Dec
        Dec_sign = Dec_sign_str
        Dec_d = int (Dec_d_str)
        Dec_m = int (Dec_m_str)
        Dec_s = int (Dec_s_str)
        Dec = "%s%02d:%02d:%02d" % (Dec_sign, Dec_d, Dec_m, Dec_s)
        # galactic longitude
        glon = float (glon_str)
        # galactic latitude
        glat = float (glat_str)
        # V-band magnitude
        Vmag = float (Vmag_str)
    
        # making 2-dim. dictionary to store data
        bsc[hr] = {}
        bsc[hr]['RA']   = RA
        bsc[hr]['Dec']  = Dec
        bsc[hr]['glon'] = glon
        bsc[hr]['glat'] = glat
        bsc[hr]['Vmag'] = Vmag

# opening file for writing
with open (file_output, 'w') as fh_out:
    # sorting data by V-band magnitude
    for obj in sorted (bsc, key=lambda x: bsc[x]['Vmag']):
        # writing data
        fh_out.write (f'{obj:4d} {bsc[obj]["RA"]:10s} {bsc[obj]["Dec"]:9s}'
                      + f' {bsc[obj]["glon"]:6.2f} {bsc[obj]["glat"]:6.2f}'
                      + f' {bsc[obj]["Vmag"]:5.2f}\n')
