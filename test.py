import vision
import matplotlib.pyplot as plt
import numpy as np

raw  = vision.raw_img(480,360)
grey = vision.greyscale(raw)
blr  = vision.gaussian_blur(grey,3,1.5)
sbl  = vision.sobel(grey)


fig = plt.gcf()
for i,a in enumerate(['raw','grey','blr','sbl']):
    ax = fig.add_subplot(2,2,i+1)
    ax.imshow(locals()[a], cmap='gray' if a!='raw' else 'jet')
    ax.set_title(a)

plt.show()
