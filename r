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

(*update with: [`cat pydoc3 vision >> README.m`]*)
