import vision
import matplotlib.pyplot as plt
import numpy as np
import sys

#chess = np.load("chess.npy")
chess = vision.rawImg(480, 360)
chess = vision.greyscale(chess)
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
            #sbl[:, c] = np.ones(sbl.shape[0]) * 255
            inCol = True
            boardCols.append(c)
    else:
        inCol = False
	

for r in range(sbl.shape[0]):
    if np.sum(sbl[r]) > int(sys.argv[2]):
        if not inRow:
            #sbl[r] = np.ones(sbl.shape[1]) * 255
            inRow = True
            boardRows.append(r)
    else:
        inRow = False

print(boardCols)
print(boardRows)

leftEdge = boardCols[1]
rightEdge = boardCols[-2]
topEdge = boardRows[1]
bottomEdge = boardRows[-2]

sqrSize = int(((rightEdge-leftEdge) + (bottomEdge-topEdge))/16) #dividing by 2 to get average then 8 as 8 squares
sqrBorder = 10

rois = [[x for x in range(8)] for y in range(8)]

for y in range(8):
    for x in range(8):
        roi = sbl[topEdge+(y*sqrSize)+sqrBorder:topEdge+((y+1)*sqrSize)-sqrBorder, leftEdge+(x*sqrSize)+sqrBorder:leftEdge+((x+1)*sqrSize)-sqrBorder] 
        rois[y][x] = np.sum(roi)
        sbl[topEdge+(y*sqrSize)+sqrBorder:topEdge+((y+1)*sqrSize)-sqrBorder, leftEdge+(x*sqrSize)+sqrBorder:leftEdge+((x+1)*sqrSize)-sqrBorder] = 120
        #print(x, y, np.sum(roi))

print("sqrSize", sqrSize)

[print(''.join([str(int(c)).rjust(6) for c in r])) for r in rois]

sbl[:, leftEdge] = 255
sbl[:, rightEdge] = 255
sbl[topEdge] = 255
sbl[bottomEdge] = 255
plt.imshow(sbl, cmap="gray")
plt.show()
