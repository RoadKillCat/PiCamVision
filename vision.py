"""Computer Vision library for Python-3.x

Support only for RPI camera module"""

import picamera
import picamera.array
import numpy as np
import matplotlib.pyplot as plt
import math, time

def getRawImg():
	"""Returns numpy array of the raw camera data of size 1663x1232"""
	with picamera.PiCamera() as camera:
		camera.resolution = (1664, 1232)#(768, 480)#(1664, 1232)
		output = np.empty((1232, 1664, 3), dtype = np.uint8)	
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
	return [[v/weightSum for v in r] for r in weightMatrix]
