import vision
import matplotlib.pyplot as plt
import numpy as np
import sys

chess = np.load("chess.npy")
blr = vision.gaussianBlur(chess, 3, 1.5)
sbl = vision.sobel(blr)

print(sys.argv[1], sys.argv[2])

boardCols =[]
boardRows = []
inRol = False
inCol = False

for c in range(sbl.shape[1]):
    if np.sum(sbl[:, c]) > int(sys.argv[1]):
        if not inCol:
            sbl[:, c] = np.ones(sbl.shape[0]) * 255
            inCol = True
            boardCols.append(c)
    else:
        inCol = False
	

for r in range(sbl.shape[0]):
    if np.sum(sbl[r]) > int(sys.argv[2]):
        if not inRow:
            sbl[r] = np.ones(sbl.shape[1]) * 255
            inRow = True
            boardRows.append(r)
    else:
        inRow = False

print(boardCols)
print(boardRows)
plt.imshow(sbl, cmap="gray")
plt.show()
