#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/11/12 09:50:03 (UT+8) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/brettonw/YaleBrightStarCatalog.git'

# directory name of downloaded repository
dir_repo = 'bsc'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
