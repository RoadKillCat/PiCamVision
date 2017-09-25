# Source for a python raspberry pi computer vision library

Installation instructions:

1. Download *vision.py*
2. Open *python* in that directory
3. Run *import vision*

Dependencies:

- [picamera](https://picamera.readthedocs.io/en/release-1.13/)
- [numpy](http://www.numpy.org/)


Contents of *help(vision)*:

    Help on module vision:

    NAME
        vision - Computer Vision library for Python-3.x

    DESCRIPTION
        Support only for RPI camera module

    FUNCTIONS
        convertToGreyscale(img)
            Returns img conveted to greyscale
        
        getKernel(size, sigma)
            Returns Kernel matrix required for Gaussian Blur
        
        getRawImg()
            Returns numpy array of the raw camera data of size 1663x1232
    
    FILE
        /home/pi/PiCamVision/vision.py
    
    (END)

