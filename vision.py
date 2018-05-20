"""Computer Vision Library for Python-3.x
Support only for rpi camera module"""

import numpy as np
import math

def raw_img(x, y):
    "Returns numpy array of the raw camera data of size (aspect 4:3)"
    try:
        import picamera
    except ImportError:
        print("sorry, picamera is not installed")
        return
    x = int(32*math.ceil(x/32))
    y = int(16*math.ceil(y/16))
    with picamera.PiCamera() as camera:
        camera.resolution = (x, y)
        output = np.empty((y, x, 3), dtype="uint8")
        camera.capture(output, "rgb")
        return output

def greyscale(img):
    "Returns img conveted to greyscale"
    return np.dot(img, [0.2126, 0.7152, 0.0722])

def gaussian_kernel(size, sigma, two_d=True):
    if two_d:
        kernel = np.fromfunction(lambda x, y: (1/(2*math.pi*sigma**2)) * math.e ** ((-1*((x-(size-1)/2)**2+(y-(size-1)/2)**2))/(2*sigma**2)), (size, size))
    else:
        kernel = np.fromfunction(lambda x: math.e ** ((-1*(x-(size-1)/2)**2) / (2*sigma**2)), (size,))
    return kernel / np.sum(kernel)

def gaussian_blur(img, k_size, k_sigma):
    kernel = gaussian_kernel(k_size, k_sigma, False)
    gaus_x = np.zeros((img.shape[0], img.shape[1] - k_size + 1), dtype="float64") # kernel[0][0] * img[:, :img.shape[1]-k_size+1] #np.zeros((img.shape[0]-k_size-1, img.shape[1]-k_size-1))
    for i, v in enumerate(kernel):
        gaus_x += v * img[:, i : img.shape[1] - k_size + i + 1]
    gaus_y = np.zeros((gaus_x.shape[0] - k_size + 1, gaus_x.shape[1]))  #gaus_x[:gaus_x.shape[0]-k_size+1]
    for i, v in enumerate(kernel):
        gaus_y += v * gaus_x[i : img.shape[0]  - k_size + i + 1]
    return gaus_y

def sobel_x(img):
    sbl_h = img[:,2:] - img[:,:-2]
    sbl_v = sbl_h[:-2] + 2*sbl_h[1:-1] + sbl_h[2:]
    return sbl_v

def sobel_y(img):
    sbl_h = img[:,2:] + 2*img[:,1:-1] + img[:,:-2]
    sbl_v = sbl_h[2:] - sbl_h[:-2]
    return sbl_v

def sobel(img, simple=False):
    "Returns a numpy array of the edges of a greyscale img, simple parameter sets whether uses absolute rather than squaring"
    if simple:
        return abs(sobel_x(img)) + abs(sobel_y(img))
    return (sobel_x(img)**2 + sobel_y(img)**2) ** 0.5

def canny(img):
    "Returns a numpy array of thinned edges with double threshold from sobel operators"
    sbl = sobel(img, True)
    can = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
    for y in range(1, sbl.shape[0]-1):
        for x in range(1,sbl.shape[1]-1):
            theta = math.atan2(sbl[y][x][0], sbl[y][x][1]) * (180 / math.pi)
            edge = int(45 * round(theta/45))
            if edge == 0:
                can[y][x] = sbl[y][x][2] if sbl[y][x][2] > sbl[y][x-1][2] and sbl[y][x][2] > sbl[y][x+1][2] else 0
            elif edge == 45:
                can[y][x] = sbl[y][x][2] if sbl[y][x][2] > sbl[y-1][x-1][2] and sbl[y][x][2] > sbl[y+1][x+1][2] else 0
            elif edge == 90:
                can[y][x] = sbl[y][x][2] if sbl[y][x][2] > sbl[y-1][x][2] and sbl[y][x][2] > sbl[y+1][x][2] else 0
            elif edge == 135:
                can[y][x] = sbl[y][x][2] if sbl[y][x][2] > sbl[y-1][x+1] and sbl[y][x][2] > sbl[y+1][x-1][2] else 0
    return can
