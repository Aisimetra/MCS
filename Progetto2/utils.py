import numpy as np
from numpy.core.fromnumeric import shape
from numpy.core.shape_base import block
import scipy
from scipy.fft import fft, dct, idct


# Read Images

def block_division(image, F):
    blocks = []
    N,M = np.shape(image)
    for i in range(0, N, F):
        if(F + i > len(image)):
            break
        for j in range(0, M, F):
            if(F + j > len(image[0])):
                continue
            blocks.append(image[0 + i: F + i, 0 + j: F + j])

    return blocks


def dct_idct_blocks (blocks, d):
    # vado a prendere blocco per blocco 
    N, M = np.shape(blocks[0])
    for p in range(len(blocks)): 
        # applico la dct ad ogni blocco e la metto sottoforma di matrice perchè mi restituisce una tupla altrimenti
        blocks[p] = scipy.fft.dct(blocks[p], type=2, norm="ortho")
        # scorro secondo le frequenze
        for k in range(N): # c_riga k
            for l in range(M): # c_colonna l
                if (k+l)>= d:
                    blocks[p][k,l] = 0   
    
    # a questo punti mi ritorna una lista di array -> da portare in matrici quindi 
    for q in range(len(blocks)): 
        blocks[q] = scipy.fft.idct(blocks[q], type=2, norm="ortho")
        for j in range (0, N):
            for l in range (0, M):
                element = blocks[q][j,l]
                blocks[q][j,l] = np.round(element)        
                if(element < 0):
                    blocks[q][j,l] = 0
                elif(element > 255):
                    blocks[q][j,l] = 255

    return blocks

#lista con tutti i blocchi a cui abbiamo gia effettuato il taglio (manteniamo sempre lo stesso ordine!)
#costruzione riga per riga, poi append finale
def rebuild(ffs, blocks_per_row):
    rebuild_mat = [ffs[0]]
    i = 0
    count_blocks_per_row = 1 
    for ff in ffs[1:]:
        if count_blocks_per_row == blocks_per_row:
            count_blocks_per_row = 0
            i = i + 1
            rebuild_mat = rebuild_mat + [ff]
        else:
            rebuild_mat[i] = np.concatenate((rebuild_mat[i], ff), axis=1)
        count_blocks_per_row = count_blocks_per_row + 1
    final_mat = rebuild_mat[0]
    for row in rebuild_mat[1:]:
        final_mat = np.concatenate((final_mat, row), axis=0)
    
    return final_mat

def frequency_cut(blocco, d):
    N,M = np.shape(blocco)
    blocco = scipy.fft.dctn(blocco, type=2, norm="ortho")
    for i in range(N):
        for j in range(M):
            if i+j >= d:
                blocco[i,j] = 0
    blocco = scipy.fft.idctn(blocco, type=2, norm="ortho")
    for i in range(N):
        for j in range(M):
            blocco[i,j] = np.round(blocco[i,j])
            if blocco[i,j] < 0:
                blocco[i,j] = 0
            if blocco[i,j] > 255:
                blocco[i,j] = 255
    return blocco


