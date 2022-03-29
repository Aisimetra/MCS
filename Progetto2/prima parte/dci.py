import math
import numpy as np

#create some X to use

def createX(N):
  listX = [None] * N
  for x in range(N):
    listX[x] = (2 * (x + 1) - 1) / (2 * N)
  return listX


#create a base W
def createW(listX):
  listW = [None] * len(listX)
  for k in range(len(listX)):
    w_j = [None] *  len(listX)
    i = 0
    for j in w_j:
      w_j[i] = math.cos(k * math.pi * listX[i])
      i = i + 1
    listW[k] = w_j
  return np.array(listW)


#generate canonical base
def generateE(N):
  listE = [None] * N
  i = 0
  for e in range(N):
    e_vector = [None] * N
    for index in range(len(e_vector)):
      if index == i:
        e_vector[index] = 1
      else:
        e_vector[index] = 0
    listE[i] = e_vector
    i = i + 1
  return np.array(listE)

      
#w^k * w^q = w1k*w1q + w2k*w2q....

def generateC(vector):
  c_values = [None] * len(vector)
  N = len(c_values)
  for index in range(N):
    if index == 0:
      alfa_k = 1 / math.sqrt(N) 
    else:
      alfa_k = math.sqrt(2/N)
    sommatory = 0
    for j in range(N):
      sommatory = sommatory + ( math.cos(index * math.pi * ((2* (j + 1) - 1) / (2 * N))) * vector[j])
    c_values[index] = alfa_k * sommatory  
  return c_values


def compute_comb1(w1_base, c_vector):
    final_vect = np.zeros(len(c_vector))
    for i in range(len(c_vector)):
      final_vect = final_vect + (c_vector[i] * w1_base[i])
    return final_vect



