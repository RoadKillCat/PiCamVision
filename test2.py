import vision
import numpy as np
import matplotlib.pyplot as plt

grey = np.load("chess.npy")
#sbl = vision.sobel(grey)

testImg = np.array([
[255, 255, 255, 255, 255],
[0,   0,   0,   0,   0  ],
[0,   0,   0,   0,   0  ],
[0,   0,   0,   0,   0  ],
[255, 255, 255, 255, 255]])
