import vision
import numpy as np
import matplotlib.pyplot as plt

img = vision.getRawImg(480, 360)
grey = vision.convertToGreyscale(img)

