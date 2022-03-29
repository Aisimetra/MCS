import numpy
from scipy import io
from scipy.sparse.linalg import spsolve
from scipy.sparse import csc_matrix
import matplotlib.pylab as plt
import numpy as np
from numpy import linalg as LA
import time

# N.B. once a matrix has been constructed, 
# convert to CSR or CSC format for fast arithmetic 
# and matrix vector operations
# consider using the COO format when constructing large matrices

def solve_linear(matrix):
    #Load sparse matrix
    A = io.mmread(matrix)

    #Plot the spy of the matrix
    #plt.spy(A)
    #plt.show()

    #Starting time
    start = time.time()

    #Exact solution
    matrix_size = A.shape
    xe = np.ones((matrix_size[0],1))

    #Compute value of b
    b = A * xe

    #Compress matrix
    A = csc_matrix(A)
    b = csc_matrix(b)

    #Solve linear system
    x = spsolve(A, b, use_umfpack = True)

    #End time
    el_time = time.time() - start 

    #Relative error
    err = LA.norm(numpy.subtract(x, xe)) / LA.norm(xe)

    return err, el_time
