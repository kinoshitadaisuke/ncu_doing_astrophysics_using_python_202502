#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/08 20:16:09 (CST) daisuke>
#

# importing subprocess module
import subprocess

# ffmpeg command
ffmpeg = 'ffmpeg'

# frame rate
framerate = 30

# number of threads
n_thread = 1

# ffmpeg options
options_ffmpeg = f'-f image2 -i solsys_3d2/%06d.png -start_number 0' \
    + f' -framerate {framerate} -an -vcodec libx264 -pix_fmt yuv420p' \
    + f' -threads {n_thread}'

# output file name
file_output = 'solsys_3d2.mp4'

# command to be executed
command_ffmpeg = f'{ffmpeg} {options_ffmpeg} {file_output}'

# execution of command
subprocess.run (command_ffmpeg, shell=True)
