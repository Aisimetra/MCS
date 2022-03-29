from utils import block_division, dct_idct_blocks, rebuild, frequency_cut
from interface  import interface_def
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# data = [F, d, path]
data = interface_def()

image = mpimg.imread(data[2])

M = np.shape(image)[1]

blocks_per_row = int(M / data[0])

blocks = block_division(image, data[0])

for i in range(len(blocks)):
    blocks[i] = frequency_cut(blocks[i], data[1])
bRebuild = rebuild(blocks, blocks_per_row)#ricambialo!

fig=plt.figure(figsize=(20, 10))

fig.add_subplot(1, 2, 1)
plt.imshow(image)
fig.add_subplot(1, 2, 2)
plt.imshow(bRebuild)
plt.show()