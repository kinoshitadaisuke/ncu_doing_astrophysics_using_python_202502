#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/29 12:21:03 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# file name
file_fig = 'appy_s14_02_06.png'

# date/time
t_str = '2025-07-01T12:00:00'
t     = astropy.time.Time (t_str, scale='utc', format='isot')

# target list
# Sun, Mercury, Venus, Earth, Mars, Jupiter
dic_target = {
    '10':  'Sun',
    '199': 'Mercury',
    '299': 'Venus',
    '399': 'Earth',
    '499': 'Mars',
    '599': 'Jupiter',
}

# marker size and colour
sizes   = [10, 2, 5, 5, 4, 8]
colours = ['yellow', 'blue', 'gold', 'green', 'red', 'orange']

# number of asteroids to be plotted
n_asteroids = 500

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('X [au]')
ax.set_ylabel ('Y [au]')

# axes
ax.set_xlim (-5.5, 5.5)
ax.set_ylim (-5.5, 5.5)
ax.set_aspect('equal')
ax.grid ()

# printing status
print (f'Now, retrieving positions of the Sun and planets...')

# getting positions of the Sun and planets
for i,n in enumerate (dic_target):
    # querying JPL Horizons
    obj = astroquery.jplhorizons.Horizons (id=n, \
                                           id_type=None, \
                                           location='@ssb', \
                                           epochs=t.jd)
    
    # state vector of the target object
    vec = obj.vectors ()

    # plotting data
    ax.plot (vec['x'], vec['y'], linestyle='None', \
             marker='o', markersize=sizes[i], color=colours[i], \
             label=dic_target[n])

# printing status
print (f'Finished retrieving positions of the Sun and planets!')

# printing status
print (f'Now, retrieving positions of asteroids...')

# empty numpy array to store data
asteroid_x = numpy.array ([])
asteroid_y = numpy.array ([])
    
# getting positions of asteroids
for i in range (n_asteroids):
    # querying JPL Horizons
    i_str = str (i + 1)
    if ( (i + 1) % 50 == 0):
        print (f"  progress: {i + 1:6d} / {n_asteroids:6d}")

    # query for Horizons System
    obj = astroquery.jplhorizons.Horizons (id=i_str, \
                                           id_type='smallbody', \
                                           location='@ssb', \
                                           epochs=t.jd)

    # state vector of the target object
    vec = obj.vectors ()

    # appending data to numpy arrays
    asteroid_x = numpy.append (asteroid_x, vec['x'][0])
    asteroid_y = numpy.append (asteroid_y, vec['y'][0])

# printing status
print (f'Finished retrieving positions of asteroids!')

# showing title
ax.set_title (f'Positions of 500 asteroids on {t_str}')

# plotting asteroids
ax.plot (asteroid_x, asteroid_y, \
         linestyle='None', marker='.', markersize=1, color='purple', \
         label='asteroids')
    
# showing legend
ax.legend (bbox_to_anchor=(1.01, 1.00), loc='upper left', shadow=True)

# saving the plot into a file
fig.savefig (file_fig, dpi=150)
