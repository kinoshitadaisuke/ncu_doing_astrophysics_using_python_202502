#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/13 10:01:01 (UT+08:00) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction of parser object for argparse
descr  = 'selecting stars by distance criteria'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input VOTable file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-a', '--min', type=float, help='minimum distance value')
parser.add_argument ('-b', '--max', type=float, help='maximum distance value')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_votable = args.input
file_output  = args.output
dist_min     = args.min
dist_max     = args.max

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# data
data_id        = numpy.array (table['SOURCE_ID'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_rv        = numpy.array (table['radial_velocity'])
data_b         = numpy.array (table['phot_bp_mean_mag'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_r         = numpy.array (table['phot_rp_mean_mag'])
data_br        = numpy.array (table['bp_rp'])
data_bg        = numpy.array (table['bp_g'])
data_gr        = numpy.array (table['g_rp'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_ra_err    = numpy.array (table['ra_error'])
data_dec_err   = numpy.array (table['dec_error'])
data_pmra_err  = numpy.array (table['pmra_error'])
data_pmdec_err = numpy.array (table['pmdec_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])

# distance
data_distance = numpy.array ([])
for i in range ( len (data_parallax) ):
    # rejecting stars of negative parallax, no measurement of parallax,
    # and parallax SNR less than 10.0
    if ( (data_parallax[i] <= 0.0) or (numpy.isnan (data_parallax[i]) ) \
         or (data_p_snr[i] < 10.0) ):
        data_distance = numpy.append (data_distance, -1.0)
    else:
        data_distance = numpy.append (data_distance, 1000.0 / data_parallax[i])

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = f'# star ID, RA, Dec, parallax, pmra, pmdec, radial velocity' \
        + f' b mag, g mag, r mag, b-r, b-g, g-r\n'
    fh.write (header)
    # examining each star
    for i in range ( len (data_distance) ):
        # rejecting stars of low signal-to-noise ratio
        if (data_b_snr[i] < 10.0):
            continue
        if (data_g_snr[i] < 10.0):
            continue
        if (data_r_snr[i] < 10.0):
            continue
        # selecting stars between distances dist_min and dist_max
        if ( (data_distance[i] >= dist_min) \
             and (data_distance[i] <= dist_max) ):
            # writing data into file
            record = f"{data_id[i]:19d}" \
                + f" {data_ra[i]:10.6f} {data_dec[i]:+10.6f}" \
                + f" {data_parallax[i]:10.6f}" \
                + f" {data_pmra[i]:10.6f} {data_pmdec[i]:10.6f}" \
                + f" {data_rv[i]:+10.6f}" \
                + f" {data_b[i]:9.6f} {data_g[i]:9.6f} {data_r[i]:9.6f}" \
                + f" {data_br[i]:9.6f} {data_bg[i]:9.6f} {data_gr[i]:9.6f}\n"
            fh.write (record)
