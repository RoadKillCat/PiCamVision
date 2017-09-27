"""Computer Vision library for Python-3.x

Support only for RPI camera module"""

import numpy as np
import math

def getRawImg(x, y):
    """Returns numpy array of the raw camera data of size 1663x1232"""
    import picamera
    x = int(32*math.ceil(x/32))
    y = int(16*math.ceil(y/16))
    with picamera.PiCamera() as camera:
        camera.resolution = (x, y)
        output = np.empty((y, x, 3), dtype="uint8") 
        camera.capture(output, "rgb")
        return output

def convertToGreyscale(img):
    """Returns img conveted to greyscale"""
    return np.dot(img, [0.2126, 0.7152, 0.0722])

def getKernel(size, sigma):
    """Returns Kernel matrix required for Gaussian Blur"""
    bl = int((size-1)/2)
    weightMatrix = [[(1/(2*math.pi*sigma**2)) * math.e ** ((-1*(x**2+y**2))/(2*sigma**2)) for x in range(-bl,bl+1)] for y in range(-bl,bl+1)]
    weightSum = sum([sum(r) for r in weightMatrix])
    return np.array([[v/weightSum for v in r] for r in weightMatrix])

def gaussianBlur(img, kSize, kSigma):
    """Returns a numpy array of the greyscale img gaussian blurred with the size and sigma vals"""
    kernel = getKernel(kSize, kSigma)
    d = int((kSize-1)/2)
    gaussian = np.zeros(img.shape, dtype="uint8")
    for y in range(d, img.shape[0]-d):
        for x in range(d, img.shape[1]-d):
            #gaussian[y][x] = np.sum(np.multiply(img[y-d:y+d+1, x-d:x+d+1], kernel))
            for yy in range(kSize):
                for xx in range(kSize):
                    gaussian[y][x] += img[(y-d)+yy][(x-d)+xx] * kernel[-d+yy][-d+xx]
    return gaussian
