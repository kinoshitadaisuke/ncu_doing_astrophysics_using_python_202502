#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/03/13 20:17:15 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.linalg

# matrix A
A = numpy.array ( [ [3.0, 1.0], [2.0, 2.0] ] )

# printing matrix A
print (f'matrix A:\n{A}')

# eigenvalues and eigenvectors of matrix A
eigenvalvec = scipy.linalg.eig (A)

# printing eigenvalues and eigenvectors of matrix A
print (f'eigenvalues of matrix A:\n{eigenvalvec[0]}')
print (f'eigenvectors of matrix A:\n{eigenvalvec[1]}')
