#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 12:36:40 (UT+08:00) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astrocatalogs/sne-pre-1990.git'

# directory name of downloaded repository
dir_repo = 'osc_0000_1989'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
