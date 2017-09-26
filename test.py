import vision
import numpy as np
import matplotlib.pyplot as plt

img = vision.getRawImg(720, 480)
grey = vision.convertToGreyscale(img)

