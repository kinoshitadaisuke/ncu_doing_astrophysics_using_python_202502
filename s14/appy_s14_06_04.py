#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/29 19:52:34 (UT+08:00) daisuke>
#

# importing datetime module
import datetime

# importing pathlib module
import pathlib

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'trojan.data'

# directory to store PNG files
dir_png = 'trojan'

# making directory if it does not exist
path_png = pathlib.Path (dir_png)
if not (path_png.exists ()):
    path_png.mkdir (mode=0o755)

# counter
i = 0

# number of major bodies
n_major = 10
# number of minor bodies
n_minor = 5000

# opening data file
with open (file_data, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # if the line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting data
        records = line.split ('|')
        # JD
        jd = float (records[0])
        # date/time
        t = records[1]
        t_datetime = datetime.datetime.fromisoformat (t)
        YYYY = t_datetime.year

        # PNG file name
        file_png = f"{dir_png}/{dir_png}_{i:04d}.png"
        
        # making objects "fig" and "canvas"
        fig    = matplotlib.figure.Figure ()
        canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

        # making objects "ax"
        ax = fig.add_subplot (121)

        # labels
        label_x = 'X [au]'
        label_y = 'Y [au]'
        label_z = 'Z [au]'
        ax.set_xlabel (label_x)
        ax.set_ylabel (label_y)

        # axes
        ax.set_xlim (-7.0, 7.0)
        ax.set_ylim (-7.0, 7.0)
        ax.set_aspect ('equal')
        ax.grid ()
        ax.set_xticks (numpy.linspace (-6, 6, 7))
        ax.set_yticks (numpy.linspace (-6, 6, 7))

        # making empty lists for storing data
        asteroids_x = []
        asteroids_y = []
        asteroids_z = []

        # reading data
        for j in ( range (2, n_major + n_minor + 2) ):
            xyz = records[j].split (',')
            x = float (xyz[0])
            y = float (xyz[1])
            z = float (xyz[2])
            if (j == 2):
                sun, = ax.plot (x, y, color='yellow', linestyle='None', \
                                marker='o', markersize=10, label='Sun')
            elif (j == 3):
                mercury, = ax.plot (x, y, color='blue', linestyle='None', \
                                   marker='o', markersize=2, label='Mercury')
            elif (j == 4):
                venus, = ax.plot (x, y, color='gold', linestyle='None', \
                                  marker='o', markersize=3, label='Venus')
            elif (j == 5):
                earth, = ax.plot (x, y, color='green', linestyle='None', \
                                  marker='o', markersize=3, label='Earth')
            elif (j == 6):
                mars, = ax.plot (x, y, color='red', linestyle='None', \
                                 marker='o', markersize=2, label='Mars')
            elif (j == 7):
                jupiter, = ax.plot (x, y, color='orange', linestyle='None', \
                                    marker='o', markersize=8, label='Jupiter')
            elif (j == 8):
                saturn, = ax.plot (x, y, color='brown', linestyle='None', \
                                   marker='o', markersize=7, label='Saturn')
            elif (j == 9):
                uranus, = ax.plot (x, y, color='lime', linestyle='None', \
                                   marker='o', markersize=6, label='Uranus')
            elif (j == 10):
                neptune, = ax.plot (x, y, color='indigo', linestyle='None', \
                                    marker='o', markersize=6, label='Neptune')
            elif (j == 11):
                pluto, = ax.plot (x, y, color='slategrey', linestyle='None',
                                  marker='o', markersize=2, label='Pluto')
            else:
                asteroids_x.append (x)
                asteroids_y.append (y)
                asteroids_z.append (z)

        # plotting asteroids
        asteroids, = ax.plot (asteroids_x, asteroids_y, \
                              color='purple', linestyle='None', \
                              marker='.', markersize=1, \
                              label='asteroids')
        
        # showing legend and title
        ax.legend (bbox_to_anchor=(0.0, -0.36), loc='upper left', \
                   frameon=False, ncol=2, \
                   handles=[sun, mercury, venus, earth, mars, jupiter])
        title_name = "Jovian Trojan Asteroids (Year %04d)" % (YYYY)
        ax.set_title (title_name)

        # making objects "ax"
        ax = fig.add_subplot (222)

        # labels
        label_x = 'X [au]'
        label_y = 'Y [au]'
        label_z = 'Z [au]'
        ax.set_xlabel (label_x)
        ax.set_ylabel (label_z)

        # axes
        ax.set_xlim (-7.0, 7.0)
        ax.set_ylim (-5, 5)
        ax.set_aspect('equal')
        ax.grid ()
        ax.set_xticks (numpy.linspace (-6, 6, 7))
        ax.set_yticks (numpy.linspace (-4, 4, 5))

        # making empty lists for storing data
        asteroids_x = []
        asteroids_y = []
        asteroids_z = []

        # reading data
        for j in ( range (2, n_major + n_minor + 2) ):
            xyz = records[j].split (',')
            x   = float (xyz[0])
            y   = float (xyz[1])
            z   = float (xyz[2])
            if (j == 2):
                sun, = ax.plot (x, z, color='yellow', linestyle='None', \
                                marker='o', markersize=10, label='Sun')
            elif (j == 3):
                mercury, = ax.plot (x, z, color='blue', linestyle='None', \
                                   marker='o', markersize=2, label='Mercury')
            elif (j == 4):
                venus, = ax.plot (x, z, color='gold', linestyle='None', \
                                  marker='o', markersize=3, label='Venus')
            elif (j == 5):
                earth, = ax.plot (x, z, color='green', linestyle='None', \
                                  marker='o', markersize=3, label='Earth')
            elif (j == 6):
                mars, = ax.plot (x, z, color='red', linestyle='None', \
                                 marker='o', markersize=2, label='Mars')
            elif (j == 7):
                jupiter, = ax.plot (x, z, color='orange', linestyle='None', \
                                    marker='o', markersize=8, label='Jupiter')
            elif (j == 8):
                saturn, = ax.plot (x, z, color='brown', linestyle='None', \
                                   marker='o', markersize=7, label='Saturn')
            elif (j == 9):
                uranus, = ax.plot (x, z, color='lime', linestyle='None', \
                                   marker='o', markersize=6, label='Uranus')
            elif (j == 10):
                neptune, = ax.plot (x, z, color='indigo', linestyle='None', \
                                    marker='o', markersize=6, label='Neptune')
            elif (j == 11):
                pluto, = ax.plot (x, z, color='slategrey', linestyle='None',
                                  marker='o', markersize=2, label='Pluto')
            else:
                asteroids_x.append (x)
                asteroids_y.append (y)
                asteroids_z.append (z)

        # plotting asteroids
        asteroids, = ax.plot (asteroids_x, asteroids_z, \
                              color='purple', linestyle='None', \
                              marker='.', markersize=1, \
                              label='asteroids')
        
        # making objects "ax"
        ax = fig.add_subplot (224)

        # labels
        label_x = 'X [au]'
        label_y = 'Y [au]'
        label_z = 'Z [au]'
        ax.set_xlabel (label_y)
        ax.set_ylabel (label_z)

        # axes
        ax.set_xlim (-7.0, 7.0)
        ax.set_ylim (-5, 5)
        ax.set_aspect('equal')
        ax.grid ()
        ax.set_xticks (numpy.linspace (-6, 6, 7))
        ax.set_yticks (numpy.linspace (-4, 4, 5))

        # making empty lists for storing data
        asteroids_x = []
        asteroids_y = []
        asteroids_z = []

        # reading data
        for j in ( range (2, n_major + n_minor + 2) ):
            xyz = records[j].split (',')
            x = float (xyz[0])
            y = float (xyz[1])
            z = float (xyz[2])
            if (j == 2):
                sun, = ax.plot (y, z, color='yellow', linestyle='None', \
                                marker='o', markersize=10, label='Sun')
            elif (j == 3):
                mercury, = ax.plot (y, z, color='blue', linestyle='None', \
                                   marker='o', markersize=2, label='Mercury')
            elif (j == 4):
                venus, = ax.plot (y, z, color='gold', linestyle='None', \
                                  marker='o', markersize=3, label='Venus')
            elif (j == 5):
                earth, = ax.plot (y, z, color='green', linestyle='None', \
                                  marker='o', markersize=3, label='Earth')
            elif (j == 6):
                mars, = ax.plot (y, z, color='red', linestyle='None', \
                                 marker='o', markersize=2, label='Mars')
            elif (j == 7):
                jupiter, = ax.plot (y, z, color='orange', linestyle='None', \
                                    marker='o', markersize=8, label='Jupiter')
            elif (j == 8):
                saturn, = ax.plot (y, z, color='brown', linestyle='None', \
                                   marker='o', markersize=7, label='Saturn')
            elif (j == 9):
                uranus, = ax.plot (y, z, color='lime', linestyle='None', \
                                   marker='o', markersize=6, label='Uranus')
            elif (j == 10):
                neptune, = ax.plot (y, z, color='indigo', linestyle='None', \
                                    marker='o', markersize=6, label='Neptune')
            elif (j == 11):
                pluto, = ax.plot (y, z, color='slategrey', linestyle='None',
                                  marker='o', markersize=2, label='Pluto')
            else:
                asteroids_x.append (x)
                asteroids_y.append (y)
                asteroids_z.append (z)

        # plotting asteroids
        asteroids, = ax.plot (asteroids_y, asteroids_z, \
                              color='purple', linestyle='None', \
                              marker='.', markersize=1, \
                              label='asteroids')
        
        ax.legend (bbox_to_anchor=(-0.3, -0.4), loc='upper left', \
                   frameon=False, ncol=2, \
                   handles=[saturn, uranus, neptune, pluto, asteroids])
        # saving the plot into a file
        fig.tight_layout ()
        fig.savefig (file_png, dpi=225)

        # increment
        i += 1
        if (i % 100 == 0):
            print (f"status: {i:6d}")
