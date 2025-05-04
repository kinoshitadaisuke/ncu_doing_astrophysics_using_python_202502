#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:32:57 (UT+08:00) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/paulfitz/exoplanets.git'

# directory name of downloaded repository
dir_repo = 'exoplanets'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
