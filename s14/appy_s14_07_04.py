#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/12/22 21:05:48 (UT+8) daisuke>
#

# importing subprocess module
import subprocess

# ffmpeg command
ffmpeg = 'ffmpeg'

# ffmpeg options
options_ffmpeg = f'-f image2 -start_number 0 -framerate 30' \
    + f' -i iss/iss_%04d.png' \
    + f' -an -vcodec libx264 -pix_fmt yuv420p -threads 4'

# output file name
file_output = 'iss.mp4'

# command to be executed
command_ffmpeg = f'{ffmpeg} {options_ffmpeg} {file_output}'

# execution of command
subprocess.run (command_ffmpeg, shell=True)
