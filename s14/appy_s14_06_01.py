#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/29 19:41:10 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# importing numpy module
import numpy

# MPC's orbital elements file
file_mpcorb = 'MPCORB.DAT.gz'

# output file
file_output = 'trojan.list'

# number of asteroids to process
n_asteroids = 5000

# dictionary to store orbital elements
dic_elements = {}

# counter
n_jt = 0

# opening file
with gzip.open (file_mpcorb, 'rb') as fh:
    # flag
    data_line = 'NO'
    # reading file
    for line in fh:
        # decoding byte data
        line = line.decode ('utf-8').strip ()
        # if line is empty, then skip
        if (line == ''):
            continue
        # reading data
        if (data_line == 'YES'):
            # number (or provisional designation)
            number = line[0:7]
            # epoch
            epoch = line[20:25]
            # mean anomaly
            M     = float (line[26:35])
            M_rad = numpy.deg2rad (M)
            # argument of perihelion
            peri     = float (line[37:46])
            peri_rad = numpy.deg2rad (peri)
            # longitude of ascending node
            node     = float (line[48:57])
            node_rad = numpy.deg2rad (node)
            # inclination
            i     = float (line[59:68])
            i_rad = numpy.deg2rad (i)
            # eccentricity
            e = float (line[70:79])
            # semimajor axis
            a = float (line[92:103])
            # orbit type
            orbit_type = line[161:165]

            # adding data to the dictionary if Jovian Trojan asteroid
            if (orbit_type == '0009'):
                dic_elements[number]         = {}
                dic_elements[number]['a']    = a
                dic_elements[number]['e']    = e
                dic_elements[number]['i']    = i_rad
                dic_elements[number]['peri'] = peri_rad
                dic_elements[number]['node'] = node_rad
                dic_elements[number]['M']    = M_rad
                # increment
                n_jt += 1

            # when finish reading expected number of asteroid data, then break
            if (n_jt >= n_asteroids):
                break
        # if the line starts with '----------'
        if (line[:10] == '----------'):
            # set the flag to 'YES'
            data_line = 'YES'
            continue

# writing data to output file
with open (file_output, 'w') as fh:
    # header of output file
    header = f'# asteroid number, a, e, i, peri, node, M\n'
    # writing header to output file
    fh.write (header)
    # for each Trojan asteroid
    for number in sorted (dic_elements.keys ()):
        # output data
        record = f"{number:8s}" \
            + f" {dic_elements[number]['a']:10.8f}" \
            + f" {dic_elements[number]['e']:10.8f}" \
            + f" {dic_elements[number]['i']:10.8f}" \
            + f" {dic_elements[number]['peri']:10.8f}" \
            + f" {dic_elements[number]['node']:10.8f}" \
            + f" {dic_elements[number]['M']:10.8f}\n"
        # writing data into output file
        fh.write (record)
