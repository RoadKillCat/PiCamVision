import vision
import matplotlib.pyplot as plt
import numpy as np
import sys

#chess = np.load("chess.npy")
raw = vision.rawImg(480, 360)
grey = vision.greyscale(raw)
blr = vision.gaussianBlur(grey, 3, 1.5)
sbl = vision.sobel(blr)

print("names of conversions are: raw, grey, blr, sbl")


plt.imshow(sbl, cmap="gray")
plt.show()
