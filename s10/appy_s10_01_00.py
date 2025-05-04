#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:13:35 (UT+08:00) daisuke>
#

# importing subprocess module
import subprocess

# URL of GitHub repository
url_repo = 'https://github.com/architecture-building-systems/honey-badger.git'

# command for downloading GitHub repository
command_git = f'git clone {url_repo}'

# downloading GitHub repository
subprocess.run (command_git, shell=True)
