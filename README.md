vision.py
=========

#### A Raspberry Pi vision library to work with the camera module

This library provides some basic functions to retrieve images from the camera module and apply operations to them. For example, you can get the raw data with `vision.raw_img` which you can then pass into `vision.greyscale` and then perform a sobel edge-detection with `vsion.sobel.

---

### Installation

1. Download `vision.py`
2. Open `python` in that directory
3. Run `import vision`

Note that this library is dependent on:

- [picamera](https://picamera.readthedocs.io/)
- [numpy](http://www.numpy.org/)

---

### Usage

This is the help page:

    NAME
        vision

    DESCRIPTION
        Computer Vision Library for Python-3.x
        Support only for rpi camera module

    FUNCTIONS
        canny(img)
            Returns a numpy array of thinned edges with double threshold from sobel operators
        
        gaussian_blur(img, kSize, kSigma)
        
        gaussian_kernel(size, sigma, two_d=True)
        
        greyscale(img)
            Returns img conveted to greyscale
        
        raw_img(x, y)
            Returns numpy array of the raw camera data of size 1663x1232
        
        sobel(img, simple=False)
            Returns a numpy array of the edges of a greyscale img, simple parameter sets whether uses absolute rather than squaring
        
        sobel_x(img)
        
        sobel_y(img)
