#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/19 12:37:39 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# input file name
file_input = 'appy_s12_00_00.data'

# output file name
file_output = 'appy_s12_00_04.data'

# shortest trial period in minute and in day
period_min_min = 10.0
period_min_day = period_min_min / (60.0 * 24.0)

# longest trial period in minute and in day
period_max_min = 300.0
period_max_day = period_max_min / (60.0 * 24.0)

# step size of trial period in minute and in day
step_min = 0.1
step_day = step_min / (60.0 * 24.0)

# number of bins for PDM analysis
n_bins = 10

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])

# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (datetime, mjd_str, mag_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        # appending the data at the end of numpy arrays
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)

# opening file for writing
with open (file_output, 'w') as fh_out:
    # writing header to output file
    header  = f"#\n"
    header += f"# parameters for PDM analysis\n"
    header += f"#\n"
    header += f"# input file                = {file_input}\n"
    header += f"# output file               = {file_output}\n"
    header += f"# shortest trial period     = {period_min_min} min\n"
    header += f"# longest trial period      = {period_max_min} min\n"
    header += f"# step size of trial period = {step_min} min\n"
    header += f"# number of bins            = {n_bins}\n"
    header += f"#\n"
    header += f"# results of PDM analysis\n"
    header += f"#\n"
    header += f"# trial period (day), trial period (hr), trial period (min), "
    header += f"total variance\n"
    header += f"#\n"
    fh_out.write (header)

    # initial value of trial period
    period_day = period_min_day

    # period search
    while (period_day < period_max_day):
        # calculation of phase with assumed period
        data_phase = numpy.array ([])
        for i in range ( len (data_mjd) ):
            phase = data_mjd[i] / period_day - int (data_mjd[i] / period_day)
            data_phase = numpy.append (data_phase, phase)
            
        # initialization of parameters
        total_variance = 0.0

        # calculation of variance
        for i in range (n_bins):
            # range of bin
            bin_min = i / n_bins
            bin_max = (i + 1) / n_bins

            # finding data within the bin
            data_bin = numpy.array ([])
            for j in range ( len (data_phase) ):
                if ( (data_phase[j] >= bin_min) and (data_phase[j] < bin_max) ):
                    data_bin = numpy.append (data_bin, data_mag[j])

            # if no data in the bin, then we skip.
            if (len (data_bin) == 0):
                continue

            # variance
            variance_in_bin = numpy.var (data_bin)
            # sum of variance
            total_variance += variance_in_bin

        # writing data to file
        output = f"{period_day:12.10f} {period_day * 24.0:12.8f} " \
            + f"{period_day * 24.0 * 60.0:12.6f} {total_variance:10.6f}\n"
        fh_out.write (output)

        # next trial period
        period_day += step_day
