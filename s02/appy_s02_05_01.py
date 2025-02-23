#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 16:49:07 (UT+8) daisuke>
#

# importing shutil module
import shutil

# finding the location of executable "sh"
location_sh = shutil.which ('sh')

# printing location of executable "sh"
print (f'location of command "sh"         = "{location_sh}"')

# finding the location of executable "cp"
location_cp = shutil.which ('cp')

# printing location of executable "cp"
print (f'location of command "cp"         = "{location_cp}"')

# finding the location of executable "gcc"
location_gcc = shutil.which ('gcc')

# printing location of executable "gcc"
print (f'location of command "gcc"        = "{location_gcc}"')

# finding the location of executable "xterm"
location_xterm = shutil.which ('xterm')

# printing location of executable "xterm"
print (f'location of command "xterm"      = "{location_xterm}"')

# finding the location of executable "emacs"
location_emacs = shutil.which ('emacs')

# printing location of executable "emacs"
print (f'location of command "emacs"      = "{location_emacs}"')

# finding the location of executable "python3.12"
location_python312 = shutil.which ('python3.12')

# printing location of executable "python3.12"
print (f'location of command "python3.12" = "{location_python312}"')
