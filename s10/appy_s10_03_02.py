#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/04 11:52:43 (UT+08:00) daisuke>
#

# data files (distance table and velocity table)
file_d = 'lvg_d.data'
file_v = 'lvg_v.data'

# output file name
file_output = 'lvg_dv.data'

# dictionary to store data
data_d = {}
data_v = {}

# opening file
with open (file_d, 'r') as fh_d:
    # reading distance table
    counter = 0
    for line in fh_d:
        # increment the counter if the line starts with '-'.
        if (line[0] == '-'):
            counter += 1
        # stop processing the line if the counter is smaller than 4.
        if ( (counter < 4) or (line[0] == '-') ):
            continue
        # extracting data
        name_str     = line[0:18].strip ()
        dm_str       = line[19:24].strip ()
        dm_err_str   = line[25:29].strip ()
        d_method_str = line[30:34].strip ()
        # conversion from string to float
        dm = float (dm_str)
        if (dm_err_str == ''):
            dm_err = 0.0
        else:
            dm_err = float (dm_err_str)
        # calculation of distance in Mpc
        dist_pc      = 10**(dm / 5.0 + 1.0)
        dist_Mpc     = dist_pc * 10**-6
        dist_pc_err  = 10**( (dm + dm_err) / 5.0 + 1.0 ) - dist_pc
        dist_Mpc_err = dist_pc_err * 10**-6
        # constructing dictionary
        data_d[name_str]                 = {}
        data_d[name_str]['dm']           = dm
        data_d[name_str]['dm_err']       = dm_err
        data_d[name_str]['dist_Mpc']     = dist_Mpc
        data_d[name_str]['dist_Mpc_err'] = dist_Mpc_err
        data_d[name_str]['method']       = d_method_str

# opening file
with open (file_v, 'r') as fh_v:
    # reading velocity table
    counter = 0
    for line in fh_v:
        # increment the counter if the line starts with '-'.
        if (line[0] == '-'):
            counter += 1
        # stop processing the line if the counter is smaller than 4.
        if ( (counter < 3) or (line[0] == '-') ):
            continue
        # extracting data
        name_str    = line[0:18].strip ()
        vel_str     = line[19:23].strip ()
        vel_err_str = line[24:27].strip ()
        # conversion from string to float
        vel = float (vel_str)
        if (vel_err_str == ''):
            vel_err = 0.0
        else:
            vel_err = float (vel_err_str)
        # constructing dictionary
        data_v[name_str]            = {}
        data_v[name_str]['vel']     = vel
        data_v[name_str]['vel_err'] = vel_err

with open (file_output, 'w') as fh_out:
    # writing header
    header = f"# LVG galaxies with known distance and velocity\n" \
        + f"#\n" \
        + f"#  data format\n" \
        + f"#\n" \
        + f"#   1st column : distance in Mpc\n" \
        + f"#   2nd column : distance error in Mpc\n" \
        + f"#   3rd column : velocity in km/s\n" \
        + f"#   4th column : velocity error in km/s\n" \
        + f"#   after '#'  : method of distance determination,\n" \
        + f"#                name of galaxy\n" \
        + f"#\n"
    fh_out.write (header)

    # finding galaxies with both known distance and velocity
    # sorting the data by distance
    for name in sorted (data_d, key=lambda x: data_d[x]['dist_Mpc']):
        # if a galaxy has velocity data, then we print the data.
        if name in data_v:
            # writing data
            record = f"{data_d[name]['dist_Mpc']:12.6f}" \
                + f" {data_d[name]['dist_Mpc_err']:12.6f}" \
                + f" {data_v[name]['vel']:12.6f}" \
                + f" {data_v[name]['vel_err']:12.6f}" \
                + f" # {data_d[name]['method']}, {name}\n"
            fh_out.write (record)
