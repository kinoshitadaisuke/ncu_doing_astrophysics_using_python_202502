#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/12/10 09:42:22 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing numpy module
import numpy
import numpy.random

# importing astropy module
import astropy.io
import astropy.table

# importing photutils module
import photutils.datasets

# constructing parser object
descr  = 'generating a synthetic image with artificial stars and galaxies'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-x', '--size-x', type=int, default=2048, \
                     help='image size in X-axis (default: 2048)')
parser.add_argument ('-y', '--size-y', type=int, default=2048, \
                     help='image size in Y-axis (default: 2048)')
parser.add_argument ('-n', '--nstars', type=int, default=100, \
                     help='number of stars to generate (default: 100)')
parser.add_argument ('-g', '--ngalaxies', type=int, default=10, \
                     help='number of galaxies to generate (default: 10)')
parser.add_argument ('-f', '--flux-min', type=float, default=1000.0, \
                     help='minimum flux of stars (default: 1000)')
parser.add_argument ('-p', '--fwhm-psf', type=float, default=3.5, \
                     help='FWHM of PSF in pixel (default: 3.5)')
parser.add_argument ('-d', '--fwhm-width', type=float, default=0.1, \
                     help='width of FWHM distribution in pixel (default: 0.1)')
parser.add_argument ('-q', '--fwhm-psf-gal', type=float, default=8.0, \
                     help='FWHM of galaxy PSF in pixel (default: 8)')
parser.add_argument ('-r', '--fwhm-psf-gal-width', type=float, default=4.0, \
                     help='width of FWHM distribution of galaxy PSF in pixel (default: 4)')
parser.add_argument ('-s', '--sky', type=float, default=1000.0, \
                     help='sky background level in ADU (default: 1000)')
parser.add_argument ('-e', '--sky-stddev', type=float, default=30.0, \
                     help='stddev of sky background in ADU (default: 30)')
parser.add_argument ('-o', '--output-file', default='', \
                     help='output file name')
parser.add_argument ('-l', '--log-file', default='', \
                     help='log file name')

# command-line argument analysis
args = parser.parse_args ()

# image size
image_size_x = args.size_x
image_size_y = args.size_y
image_shape  = (image_size_x, image_size_y)

# number of stars and galaxies to generate
nstars = args.nstars
ngals  = args.ngalaxies

# flux of faintest stars
flux_min = args.flux_min

# FWHM of PSF
fwhm_x           = args.fwhm_psf
fwhm_y           = args.fwhm_psf
fwhm_width_x     = args.fwhm_width
fwhm_width_y     = args.fwhm_width
fwhm_gal_x       = args.fwhm_psf_gal
fwhm_gal_y       = args.fwhm_psf_gal
fwhm_gal_width_x = args.fwhm_psf_gal_width
fwhm_gal_width_y = args.fwhm_psf_gal_width

# sky background level and stddev
sky_mean   = args.sky
sky_stddev = args.sky_stddev

# output file name and log file name
file_output = args.output_file
file_log    = args.log_file

# making pathlib objects
path_output = pathlib.Path (file_output)
path_log    = pathlib.Path (file_log)

# check of output file name
if not (path_output.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file must be a FITS file.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# check of log file name
if (file_log == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: You need to specify log file name.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# existence check for output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: output file "{file_output}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# existence check for log file
if (path_log.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: log file "{file_log}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# printing status
print (f'Now, generating source table for stars and galaxies...')

# PSF model
psf_model = astropy.modeling.models.Gaussian2D ()

# making source table for stars
flux_max   = flux_min * 30.0
fwhm_x_min = fwhm_x - fwhm_width_x
fwhm_x_max = fwhm_x + fwhm_width_x
fwhm_y_min = fwhm_y - fwhm_width_y
fwhm_y_max = fwhm_y + fwhm_width_y
stars = photutils.datasets.make_model_params (image_shape, \
                                              nstars, \
                                              x_name='x_mean', \
                                              y_name='y_mean', \
                                              min_separation=10.0, \
                                              amplitude=(flux_min, \
                                                         flux_max), \
                                              x_stddev=(fwhm_x_min, \
                                                        fwhm_x_max), \
                                              y_stddev=(fwhm_y_min, \
                                                        fwhm_y_max), \
                                              theta=(0.0, 2.0 * numpy.pi) )

# making source table for galaxies
flux_max       = flux_min * 50.0
fwhm_gal_x_min = fwhm_gal_x - fwhm_gal_width_x
fwhm_gal_x_max = fwhm_gal_x + fwhm_gal_width_x
fwhm_gal_y_min = fwhm_gal_y - fwhm_gal_width_y
fwhm_gal_y_max = fwhm_gal_y + fwhm_gal_width_y
galaxies = photutils.datasets.make_model_params (image_shape, \
                                                 ngals, \
                                                 x_name='x_mean', \
                                                 y_name='y_mean', \
                                                 min_separation=10.0, \
                                                 amplitude=(flux_min, \
                                                            flux_max), \
                                                 x_stddev=(fwhm_gal_x_min, \
                                                           fwhm_gal_y_max), \
                                                 y_stddev=(fwhm_gal_x_min, \
                                                           fwhm_gal_y_max), \
                                                 theta=(0.0, 2.0 * numpy.pi) )

# printing status
print (f'Finished generating source table for stars and galaxies!')

# printing status
print (f'Now, writing source table into log file...')

# writing positions of stars and galaxies to log file
with open (file_log, 'w') as fh_log:
    # information of stars
    fh_log.write (f'#\n')
    fh_log.write (f'# input parameters for producing synthetic image\n')
    fh_log.write (f'#\n')
    fh_log.write (f'#   image_size_x      = {image_size_x}\n')
    fh_log.write (f'#   image_size_y      = {image_size_y}\n')
    fh_log.write (f'#   nstars            = {nstars}\n')
    fh_log.write (f'#   ngals             = {ngals}\n')
    fh_log.write (f'#   flux_min          = {flux_min}\n')
    fh_log.write (f'#   fwhm_x            = {fwhm_x}\n')
    fh_log.write (f'#   fwhm_y            = {fwhm_y}\n')
    fh_log.write (f'#   fwhm_width_x      = {fwhm_width_x}\n')
    fh_log.write (f'#   fwhm_width_y      = {fwhm_width_y}\n')
    fh_log.write (f'#   fwhm_gal_x        = {fwhm_gal_x}\n')
    fh_log.write (f'#   fwhm_gal_y        = {fwhm_gal_y}\n')
    fh_log.write (f'#   fwhm_gal_width_x  = {fwhm_gal_width_x}\n')
    fh_log.write (f'#   fwhm_gal_width_y  = {fwhm_gal_width_y}\n')
    fh_log.write (f'#   sky_mean          = {sky_mean}\n')
    fh_log.write (f'#   sky_stddev        = {sky_stddev}\n')
    fh_log.write (f'#   file_output       = {file_output}\n')
    fh_log.write (f'#   file_log          = {file_log}\n')
    fh_log.write (f'#\n')
    fh_log.write (f'# information of stars\n')
    fh_log.write (f'#\n')
    astropy.io.ascii.write (stars, fh_log, format='commented_header')
    # information of galaxies
    fh_log.write (f'#\n')
    fh_log.write (f'# information of galaxies\n')
    fh_log.write (f'#\n')
    astropy.io.ascii.write (galaxies, fh_log, format='commented_header')

# printing status
print (f'Finished writing source table into log file!')
    
# printing status
print (f'Now, generating synthetic stars...')
    
# generating stars
image_stars = photutils.datasets.make_model_image (image_shape, \
                                                   psf_model, \
                                                   stars, \
                                                   x_name='x_mean', \
                                                   y_name='y_mean')

# printing status
print (f'Finished generating synthetic stars!')

# printing status
print (f'Now, generating synthetic galaxies...')

# generating galaxies
image_gals = photutils.datasets.make_model_image (image_shape, \
                                                  psf_model, \
                                                  galaxies, \
                                                  x_name='x_mean', \
                                                  y_name='y_mean')

# printing status
print (f'Finished generating synthetic galaxies!')

# printing status
print (f'Now, creating synthetic image...')

# generating sky background
image_sky = photutils.datasets.make_noise_image (image_shape, \
                                                 distribution='gaussian', \
                                                 mean=sky_mean, \
                                                 stddev=sky_stddev)
# generating synthetic image
image = image_stars + image_gals + image_sky

# printing status
print (f'Finished creating synthetic image!')

# printing status
print (f'Now, writing FITS file...')

# preparing a FITS header
header = astropy.io.fits.PrimaryHDU ().header

# writing a FITS file
astropy.io.fits.writeto (file_output, image, header=header)

# printing status
print (f'Finished writing FITS file!')
