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

The `live.py` script starts a `picamera` preview of the current camera view.
The `test.py` script uses `vision` functions to apply some effects to an image taken from the pi.

I have not written proper documentation for the functions themselves, but here is the help page:

(*update with: [`cat pydoc3 vision.py >> README.md`]*)

Help on module vision:

    NAME
        vision

    DESCRIPTION
        Computer Vision Library for Python-3.x
        Support only for rpi camera module

    FUNCTIONS
        gaussian_blur(img, k_size, k_sigma)
            takes a greyscale image in the form of a numpy array and blurs it with a kernel of size k-size and sigma `k_sigma`
        
        gaussian_kernel(size, sigma, two_d=True)
            returns a one-dimensional gaussian kernel if two_d is False, otherwise 2d
        
        greyscale(img)
            returns img conveted to greyscale
        
        raw_img(x, y)
            returns numpy array of the raw camera data of size (aspect 4:3)
        
        sobel(img, simple=False)
            returns a numpy array of the edges of a greyscale img, simple parameter sets whether uses absolute rather than squaring

    FILE
        /home/pi/rpi_vision/vision.py


