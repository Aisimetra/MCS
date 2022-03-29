import math
import numpy as np
import dci


def createW2(w1base):
    W2base = {}
    w1_index = 0
    w2_index = 0
    for w1 in w1base:
        for w2 in w1base:
            mat = np.zeros((len(w1), len(w1))) #cosi mette solo due righe!! deve essere N x N
            for i in range(len(w1base)):
                for j in range(len(w1base)):
                    mat[i][j] = w1[i] * w2[j]
            W2base.update({f'{w1_index},{w2_index}' : mat})
            w2_index = w2_index + 1
        w2_index = 0
        w1_index = w1_index + 1 
    return W2base
        

def generateC2(matrix):#riscrivila secondo il pdf
    N, M = np.shape(matrix)
    Cmat = np.zeros((N, M))
    for k in range(N):
        for q in range(M):
           if k == 0 and q == 0:
            alfa_k_q = 1 / np.sqrt(N * M) 
           elif k != 0 and q == 0:
            alfa_k_q = np.sqrt(2/(N * M))
           elif k == 0 and q != 0:
            alfa_k_q = np.sqrt(2/(N * M)) 
           else:
            alfa_k_q = 2/np.sqrt(N * M)
           sommatory = 0
           for i in range(N):
             for j in range(M):   
               m =  matrix[i,j] 
               cos1 = np.cos(k * np.pi * ((2 * i + 1) / (2 * N)))
               cos2 = np.cos(q * np.pi * ((2 * j + 1) / (2 * M)))
               sommatory = sommatory + (m * cos1 * cos2)
             Cmat[k][q] = alfa_k_q * sommatory
    return Cmat


def generate_example(N):
    return np.random.random_integers(low=0, high=255, size=(N,N))


def compute_comb2(ortbase2, c2matrix):
    final_mat = np.zeros((np.shape(c2matrix)[0], np.shape(c2matrix)[0]))
    i = 0
    j = 0
    for i in range(np.shape(c2matrix)[0]):
        for j in range(np.shape(c2matrix)[0]):
           final_mat = final_mat + c2matrix[i][j] * ortbase2[f'{i},{j}'] 
    return final_mat


def n3dct2(matrix):
    N, M = np.shape(matrix)
    for i in range(N):
        matrix[i] = dci.generateC(matrix[i])
    for j in range(M):
        matrix[:,j] = dci.generateC(matrix[:,j])
    return matrix






