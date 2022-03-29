from dci import compute_comb1, compute_comb1, createW, createX, generateC, generateE
import math
import numpy as np
import dci2
import time
import matplotlib.pyplot as plt

import scipy.fftpack

#DCT IMPLEMANTATA DA NOI
example_vect = [231, 32, 233, 161, 24, 71, 140, 245] 
c1_values = generateC(example_vect)
#print(c1_values)

#DCT del pacchetto scipy
c1_scipy = scipy.fftpack.dct(example_vect, type=2, n=None, axis=- 1, norm='ortho', overwrite_x=False)
#print(a)


#DCT2 IMPLEMENTATA DA NOI
example_mat = np.matrix([[231, 32, 233, 161, 24, 71, 140, 245], [247, 40, 248, 245, 124, 204, 36, 107], [234, 202, 245, 167, 9, 217, 239, 173], [193, 190, 100, 167, 43, 180, 8, 70], [11, 24, 210, 177, 81, 243, 8, 112], [97, 195, 203, 47, 125, 114, 165, 181], [193, 70, 174, 167, 41, 30, 127, 245], [87, 149, 57, 192, 65, 129, 178, 228]])
c2_matrix = dci2.generateC2(example_mat)
#print(c2_matrix)


#DCT2 DEL PACCHETTO scipy

c2_scipy = scipy.fftpack.dct(example_mat, type=2, n=None, axis=- 1, norm='ortho', overwrite_x=False)
print(c2_scipy)

#CALCOLO DEI TEMPI
#generare matrici random:

times_ourdct = []
times_scipydct = []
dimension_ourdct = []
dimension_scipydct = []


for i in range(2,80,2):
  dimension_ourdct = dimension_ourdct + [i]
  example = (dci2.generate_example(i))
  start = time.time()
  c2_ex = dci2.generateC2(example)
  end = time.time()
  time_1 = end - start
  times_ourdct = times_ourdct + [time_1]

for i in range(2,80,2):
  dimension_scipydct = dimension_scipydct + [i]
  start2 = time.time()
  c2_scipy_ex = scipy.fftpack.dct(example, type=2, n=None, axis=- 1, norm='ortho', overwrite_x=False)
  end2 = time.time()
  time_2 = end2 - start2
  times_scipydct = times_scipydct + [time_2]

print(times_ourdct)
print(times_scipydct)

#plot grafico
plt.plot(dimension_ourdct, times_ourdct, label = 'ourdct')
plt.plot(dimension_scipydct, times_scipydct, label = 'scipydct')
plt.legend()
plt.yscale('log')
plt.title('time grow')
plt.grid(True)
plt.xlabel('N dimension of N*N matrices')
plt.ylabel('time in seconds')
plt.show()

